import json
import os
import shutil
import asyncio
import aiohttp
import aiodocker
import zipfile
import re
import logging
from datetime import datetime

from .exceptions import ConnectionError, ApiError, SpecificationError
from aiodocker.exceptions import DockerError


VPN_IMAGE = "trainml/tinc:no-upnp"
STORAGE_IMAGE = "trainml/local-storage"
STATUSES = dict(
    UNKNOWN="unknown",
    NEW="new",
    CONNECTING="connecting",
    CONNECTED="connected",
    NOT_CONNECTED="not connected",
    STOPPED="stopped",
    REMOVED="removed",
)


class Connections(object):
    def __init__(self, trainml):
        self.trainml = trainml
        CONFIG_DIR = os.path.expanduser(
            os.environ.get("TRAINML_CONFIG_DIR") or "~/.trainml"
        )
        self.dir = f"{CONFIG_DIR}/connections"
        os.makedirs(
            self.dir,
            exist_ok=True,
        )

    async def list(self):
        con_dirs = os.listdir(self.dir)
        connections = []
        con_tasks = []
        for con_dir in con_dirs:
            try:
                con_type, con_id = con_dir.split("_")
            except ValueError:
                # unintelligible directory
                continue
            connection = Connection(self.trainml, con_type, con_id)
            connections.append(connection)
            con_task = asyncio.create_task(connection.check())
            con_tasks.append(con_task)
        await asyncio.gather(*con_tasks)
        return connections

    async def cleanup(self):
        con_dirs = os.listdir(self.dir)
        await asyncio.gather(
            asyncio.create_task(
                _cleanup_containers(self.dir, con_dirs, "vpn")
            ),
            asyncio.create_task(
                _cleanup_containers(self.dir, con_dirs, "storage")
            ),
        )

    async def remove_all(self):
        shutil.rmtree(self.dir)
        os.makedirs(
            self.dir,
            exist_ok=True,
        )
        await self.cleanup()


class Connection:
    def __init__(self, trainml, entity_type, id, entity=None, **kwargs):
        self.trainml = trainml
        self._id = id
        self._type = entity_type
        self._status = STATUSES.get("UNKNOWN")
        self._entity = entity
        CONFIG_DIR = os.path.expanduser(
            os.environ.get("TRAINML_CONFIG_DIR") or "~/.trainml"
        )
        CONNECTIONS_DIR = f"{CONFIG_DIR}/connections"
        self._dir = f"{CONNECTIONS_DIR}/{entity_type}_{id}"
        os.makedirs(
            self._dir,
            exist_ok=True,
        )

    @property
    def id(self) -> str:
        return self._id

    @property
    def type(self) -> str:
        return self._type

    @property
    def status(self) -> str:
        return self._status

    def __str__(self):
        return f"Connection for {self.type} - {self.id}: {self.status}"

    def __repr__(self):
        return f"Connection( trainml , {self.id}, {self.type})"

    async def _get_entity(self):
        if self.type == "dataset":
            self._entity = await self.trainml.datasets.get(self.id)
        elif self.type == "job":
            self._entity = await self.trainml.jobs.get(self.id)
        elif self.type == "model":
            self._entity = await self.trainml.models.get(self.id)
        else:
            raise TypeError(
                "Connection type must be in: ['dataset', 'model', 'job']"
            )

    async def _download_connection_details(self):
        zip_file = f"{self._dir}/details.zip"
        url = await self._entity.get_connection_utility_url()
        async with aiohttp.ClientSession() as session:
            async with session.request("GET", url) as resp:
                with open(
                    zip_file,
                    "wb",
                ) as fd:
                    content = await resp.read()
                    fd.write(content)
        with zipfile.ZipFile(zip_file, "r") as zipf:
            for info in zipf.infolist():
                extracted_path = zipf.extract(info, self._dir)
                if info.create_system == 3 and os.path.isfile(
                    extracted_path
                ):  ## 3 - ZIP_UNIX_SYSTEM
                    unix_attributes = info.external_attr >> 16
                    if unix_attributes:
                        os.chmod(extracted_path, unix_attributes)

        os.remove(zip_file)

    async def _test_connection(self, container):
        entity_details = self._entity.get_connection_details()
        if not entity_details:
            return False
        net = _parse_cidr(entity_details.get("cidr"))
        target_ip = f"{net.get('first_octet')}.{net.get('second_octet')}.{net.get('third_octet')}.254"

        logging.debug("")
        ping = await container.exec(
            ["ping", "-c", "1", target_ip],
            stdout=True,
            stderr=True,
        )
        stream = ping.start()
        await stream.read_out()
        data = await ping.inspect()
        while data["ExitCode"] is None:
            await stream.read_out()
            data = await ping.inspect()
        await stream.close()
        if data["ExitCode"] == 0:
            return True
        return False

    async def check(self):
        if not self._entity:
            try:
                await self._get_entity()
            except ApiError as e:
                if e.status == 404:
                    self._status = STATUSES.get("REMOVED")
                    self._status = STATUSES.get("REMOVED")
                    shutil.rmtree(self._dir)
                else:
                    raise e
        if not os.path.isdir(f"{self._dir}/data"):
            self._status = STATUSES.get("NEW")
            return

        try:
            with open(f"{self._dir}/vpn_id", "r") as f:
                vpn_id = f.read()
        except OSError as e:
            self._status = STATUSES.get("STOPPED")
            return

        docker = aiodocker.Docker()
        try:
            container = await docker.containers.get(vpn_id)
        except DockerError as e:
            if e.status == 404:
                self._status = STATUSES.get("STOPPED")
                await docker.close()
                return
            raise e

        data = await container.show()
        if not data["State"]["Running"]:
            self._status = STATUSES.get("STOPPED")
            await container.delete()
            os.remove(f"{self._dir}/vpn_id")
            try:
                with open(f"{self._dir}/storage_id", "r") as f:
                    storage_id = f.read()
                try:
                    storage_container = await docker.containers.get(storage_id)
                    await storage_container.delete(force=True)
                except DockerError as e:
                    if e.status != 404:
                        raise e
            except OSError as e:
                pass
            await docker.close()
            return

        connected = await self._test_connection(container)
        await docker.close()
        if connected:
            self._status = STATUSES.get("CONNECTED")
        else:
            self._status = STATUSES.get("NOT_CONNECTED")

    async def start(self):
        logging.debug(f"Beginning start {self.type} connection {self.id}")
        if self.status == STATUSES.get("UNKNOWN"):
            await self.check()
        if self.status in [
            STATUSES.get("CONNECTING"),
            STATUSES.get("CONNECTED"),
            STATUSES.get("NOT_CONNECTED"),
        ]:
            raise SpecificationError(
                "status", "Only inactive connections can be started."
            )
        self._status = STATUSES.get("CONNECTING")
        logging.info(f"Connecting...")
        if not self._entity:
            await self._get_entity()
        if not os.path.isdir(f"{self._dir}/data"):
            await self._download_connection_details()

        docker = aiodocker.Docker()
        await asyncio.gather(
            docker.pull(VPN_IMAGE), docker.pull(STORAGE_IMAGE)
        )
        entity_details = self._entity.get_connection_details()
        if (
            entity_details.get("model_path")
            or entity_details.get("input_path")
            or entity_details.get("output_path")
        ):
            logging.debug(f"Starting storage container")
            storage_container = await docker.containers.run(
                _get_storage_container_config(
                    self.id,
                    entity_details.get("cidr"),
                    f"{self._dir}/data",
                    entity_details.get("ssh_port"),
                    model_path=entity_details.get("model_path"),
                    input_path=entity_details.get("input_path"),
                    output_path=entity_details.get("output_path"),
                )
            )
            logging.debug(
                f"Storage container started, id: {storage_container.id}"
            )
            with open(f"{self._dir}/storage_id", "w") as f:
                f.write(storage_container.id)

        logging.debug(f"Starting VPN container")
        vpn_container = await docker.containers.run(
            _get_vpn_container_config(
                self.id, entity_details.get("cidr"), f"{self._dir}/data"
            )
        )
        logging.debug(f"VPN container started, id: {vpn_container.id}")

        with open(f"{self._dir}/vpn_id", "w") as f:
            f.write(vpn_container.id)

        count = 0
        while count <= 30:
            logging.debug(f"Test connectivity attempt {count+1}")
            res = await self._test_connection(vpn_container)
            if res:
                logging.debug(f"Test connectivity successful {count+1}")
                break
            count += 1
        await docker.close()
        if count > 30:
            self._status = STATUSES.get("NOT_CONNECTED")
            raise ConnectionError(f"Unable to connect {self.type} {self.id}")
        self._status = STATUSES.get("CONNECTED")
        logging.info(f"Connection Successful.")
        logging.debug(f"Completed start {self.type} connection {self.id}")

    async def stop(self):
        logging.debug(f"Beginning stop {self.type} connection {self.id}")
        if not self._entity:
            await self._get_entity()
        docker = aiodocker.Docker()
        tasks = []
        logging.info("Disconnecting...")
        try:
            with open(f"{self._dir}/vpn_id", "r") as f:
                vpn_id = f.read()
            logging.debug(f"vpn container id: {vpn_id}")
            vpn_container = await docker.containers.get(vpn_id)
            vpn_delete_task = asyncio.create_task(
                vpn_container.delete(force=True)
            )
            tasks.append(vpn_delete_task)
            os.remove(f"{self._dir}/vpn_id")
        except OSError:
            logging.debug("vpn container not found")

        storage_delete_task = None
        try:
            with open(f"{self._dir}/storage_id", "r") as f:
                storage_id = f.read()
            logging.debug(f"storage container id: {vpn_id}")
            storage_container = await docker.containers.get(storage_id)
            storage_delete_task = asyncio.create_task(
                storage_container.delete(force=True)
            )
            tasks.append(storage_delete_task)
            os.remove(f"{self._dir}/storage_id")
        except OSError:
            logging.debug("storage container not found")

        await asyncio.gather(*tasks)
        await docker.close()
        self._status = STATUSES.get("REMOVED")
        shutil.rmtree(self._dir)
        logging.info("Disconnected.")
        logging.debug(f"Completed stop {self.type} connection {self.id}")


async def _cleanup_containers(path, con_dirs, type):
    containers_target = []
    for con_dir in con_dirs:
        try:
            with open(f"{path}/{con_dir}/{type}_id", "r") as f:
                id = f.read()
            containers_target.append(id)
        except OSError:
            continue

    docker = aiodocker.Docker()
    containers = await docker.containers.list(
        all=True,
        filters=json.dumps(dict(label=["service=trainml", f"type={type}"])),
    )

    tasks = [
        asyncio.create_task(container.delete(force=True))
        for container in containers
        if container.id not in containers_target
    ]

    await asyncio.gather(*tasks)
    await docker.close()


def _parse_cidr(cidr):
    res = re.match(
        r"(?P<first_octet>[0-9]{1,3})\.(?P<second_octet>[0-9]{1,3})\.(?P<third_octet>[0-9]{1,3})\.(?P<fourth_octet>[0-9]{1,3})/(?P<mask_length>[0-9]{1,2})",
        cidr,
    )
    net = res.groupdict()
    return net


def _get_vpn_container_config(id, cidr, data_dir):
    config = dict(
        Image=VPN_IMAGE,
        Hostname=id,
        Cmd=[],
        AttachStdin=False,
        AttachStdout=False,
        AttachStderr=False,
        Tty=False,
        Env=[
            f"NETWORK={id}",
            "DEBUG=1",
        ],
        HostConfig=dict(
            Init=True,
            Binds=[f"{data_dir}:/etc/tinc:rw"],
            NetworkMode="host",
            CapAdd=["NET_ADMIN"],
        ),
        Labels=dict(type="vpn", service="trainml", id=id),
    )
    return config


def _get_storage_container_config(
    id,
    cidr,
    data_dir,
    ssh_port,
    model_path=None,
    input_path=None,
    output_path=None,
):
    Binds = [f"{data_dir}/.ssh:/opt/ssh"]
    if model_path:
        Binds.append(f"{os.path.expanduser(model_path)}:/opt/model:ro")
    if input_path:
        Binds.append(f"{os.path.expanduser(input_path)}:/opt/data:ro")
    if output_path:
        Binds.append(f"{os.path.expanduser(output_path)}:/opt/output:rw")
    config = dict(
        Image=STORAGE_IMAGE,
        Hostname=id,
        Cmd=[],
        AttachStdin=False,
        AttachStdout=False,
        AttachStderr=False,
        Tty=False,
        Env=[
            f"VPN_CIDR={cidr}",
        ],
        ExposedPorts={f"22/tcp": {}},
        HostConfig=dict(
            Init=True,
            Binds=Binds,
            PortBindings={
                f"22/tcp": [dict(HostPort=f"{ssh_port}", HostIP="0.0.0.0")],
            },
        ),
        Labels=dict(type="storage", service="trainml", id=id),
    )
    return config