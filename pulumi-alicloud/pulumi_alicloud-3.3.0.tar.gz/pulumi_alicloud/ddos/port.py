# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PortArgs', 'Port']

@pulumi.input_type
class PortArgs:
    def __init__(__self__, *,
                 frontend_port: pulumi.Input[str],
                 frontend_protocol: pulumi.Input[str],
                 instance_id: pulumi.Input[str],
                 real_servers: pulumi.Input[Sequence[pulumi.Input[str]]],
                 backend_port: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Port resource.
        :param pulumi.Input[str] frontend_port: The forwarding port.
        :param pulumi.Input[str] frontend_protocol: The forwarding protocol. Valid values `tcp` and `udp`.
        :param pulumi.Input[str] instance_id: The ID of Ddoscoo instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] real_servers: List of source IP addresses.
        :param pulumi.Input[str] backend_port: The port of the origin server.
        """
        pulumi.set(__self__, "frontend_port", frontend_port)
        pulumi.set(__self__, "frontend_protocol", frontend_protocol)
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "real_servers", real_servers)
        if backend_port is not None:
            pulumi.set(__self__, "backend_port", backend_port)

    @property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> pulumi.Input[str]:
        """
        The forwarding port.
        """
        return pulumi.get(self, "frontend_port")

    @frontend_port.setter
    def frontend_port(self, value: pulumi.Input[str]):
        pulumi.set(self, "frontend_port", value)

    @property
    @pulumi.getter(name="frontendProtocol")
    def frontend_protocol(self) -> pulumi.Input[str]:
        """
        The forwarding protocol. Valid values `tcp` and `udp`.
        """
        return pulumi.get(self, "frontend_protocol")

    @frontend_protocol.setter
    def frontend_protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "frontend_protocol", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        """
        The ID of Ddoscoo instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="realServers")
    def real_servers(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of source IP addresses.
        """
        return pulumi.get(self, "real_servers")

    @real_servers.setter
    def real_servers(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "real_servers", value)

    @property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> Optional[pulumi.Input[str]]:
        """
        The port of the origin server.
        """
        return pulumi.get(self, "backend_port")

    @backend_port.setter
    def backend_port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backend_port", value)


@pulumi.input_type
class _PortState:
    def __init__(__self__, *,
                 backend_port: Optional[pulumi.Input[str]] = None,
                 frontend_port: Optional[pulumi.Input[str]] = None,
                 frontend_protocol: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 real_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Port resources.
        :param pulumi.Input[str] backend_port: The port of the origin server.
        :param pulumi.Input[str] frontend_port: The forwarding port.
        :param pulumi.Input[str] frontend_protocol: The forwarding protocol. Valid values `tcp` and `udp`.
        :param pulumi.Input[str] instance_id: The ID of Ddoscoo instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] real_servers: List of source IP addresses.
        """
        if backend_port is not None:
            pulumi.set(__self__, "backend_port", backend_port)
        if frontend_port is not None:
            pulumi.set(__self__, "frontend_port", frontend_port)
        if frontend_protocol is not None:
            pulumi.set(__self__, "frontend_protocol", frontend_protocol)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if real_servers is not None:
            pulumi.set(__self__, "real_servers", real_servers)

    @property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> Optional[pulumi.Input[str]]:
        """
        The port of the origin server.
        """
        return pulumi.get(self, "backend_port")

    @backend_port.setter
    def backend_port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backend_port", value)

    @property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> Optional[pulumi.Input[str]]:
        """
        The forwarding port.
        """
        return pulumi.get(self, "frontend_port")

    @frontend_port.setter
    def frontend_port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "frontend_port", value)

    @property
    @pulumi.getter(name="frontendProtocol")
    def frontend_protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The forwarding protocol. Valid values `tcp` and `udp`.
        """
        return pulumi.get(self, "frontend_protocol")

    @frontend_protocol.setter
    def frontend_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "frontend_protocol", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of Ddoscoo instance.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="realServers")
    def real_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of source IP addresses.
        """
        return pulumi.get(self, "real_servers")

    @real_servers.setter
    def real_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "real_servers", value)


class Port(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_port: Optional[pulumi.Input[str]] = None,
                 frontend_port: Optional[pulumi.Input[str]] = None,
                 frontend_protocol: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 real_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Anti-DDoS Pro Port resource.

        For information about Anti-DDoS Pro Port and how to use it, see [What is Port](https://www.alibabacloud.com/help/en/doc-detail/157482.htm).

        > **NOTE:** Available in v1.123.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example_ddos_coo_instance = alicloud.ddos.DdosCooInstance("exampleDdosCooInstance",
            bandwidth="30",
            base_bandwidth="30",
            service_bandwidth="100",
            port_count="50",
            domain_count="50")
        example_port = alicloud.ddos.Port("examplePort",
            instance_id=example_ddos_coo_instance.id,
            frontend_port="7001",
            frontend_protocol="tcp",
            real_servers=[
                "1.1.1.1",
                "2.2.2.2",
            ])
        ```

        ## Import

        Anti-DDoS Pro Port can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ddos/port:Port example <instance_id>:<frontend_port>:<frontend_protocol>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backend_port: The port of the origin server.
        :param pulumi.Input[str] frontend_port: The forwarding port.
        :param pulumi.Input[str] frontend_protocol: The forwarding protocol. Valid values `tcp` and `udp`.
        :param pulumi.Input[str] instance_id: The ID of Ddoscoo instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] real_servers: List of source IP addresses.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PortArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Anti-DDoS Pro Port resource.

        For information about Anti-DDoS Pro Port and how to use it, see [What is Port](https://www.alibabacloud.com/help/en/doc-detail/157482.htm).

        > **NOTE:** Available in v1.123.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example_ddos_coo_instance = alicloud.ddos.DdosCooInstance("exampleDdosCooInstance",
            bandwidth="30",
            base_bandwidth="30",
            service_bandwidth="100",
            port_count="50",
            domain_count="50")
        example_port = alicloud.ddos.Port("examplePort",
            instance_id=example_ddos_coo_instance.id,
            frontend_port="7001",
            frontend_protocol="tcp",
            real_servers=[
                "1.1.1.1",
                "2.2.2.2",
            ])
        ```

        ## Import

        Anti-DDoS Pro Port can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ddos/port:Port example <instance_id>:<frontend_port>:<frontend_protocol>
        ```

        :param str resource_name: The name of the resource.
        :param PortArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PortArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_port: Optional[pulumi.Input[str]] = None,
                 frontend_port: Optional[pulumi.Input[str]] = None,
                 frontend_protocol: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 real_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PortArgs.__new__(PortArgs)

            __props__.__dict__["backend_port"] = backend_port
            if frontend_port is None and not opts.urn:
                raise TypeError("Missing required property 'frontend_port'")
            __props__.__dict__["frontend_port"] = frontend_port
            if frontend_protocol is None and not opts.urn:
                raise TypeError("Missing required property 'frontend_protocol'")
            __props__.__dict__["frontend_protocol"] = frontend_protocol
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            if real_servers is None and not opts.urn:
                raise TypeError("Missing required property 'real_servers'")
            __props__.__dict__["real_servers"] = real_servers
        super(Port, __self__).__init__(
            'alicloud:ddos/port:Port',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backend_port: Optional[pulumi.Input[str]] = None,
            frontend_port: Optional[pulumi.Input[str]] = None,
            frontend_protocol: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            real_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Port':
        """
        Get an existing Port resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backend_port: The port of the origin server.
        :param pulumi.Input[str] frontend_port: The forwarding port.
        :param pulumi.Input[str] frontend_protocol: The forwarding protocol. Valid values `tcp` and `udp`.
        :param pulumi.Input[str] instance_id: The ID of Ddoscoo instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] real_servers: List of source IP addresses.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PortState.__new__(_PortState)

        __props__.__dict__["backend_port"] = backend_port
        __props__.__dict__["frontend_port"] = frontend_port
        __props__.__dict__["frontend_protocol"] = frontend_protocol
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["real_servers"] = real_servers
        return Port(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backendPort")
    def backend_port(self) -> pulumi.Output[Optional[str]]:
        """
        The port of the origin server.
        """
        return pulumi.get(self, "backend_port")

    @property
    @pulumi.getter(name="frontendPort")
    def frontend_port(self) -> pulumi.Output[str]:
        """
        The forwarding port.
        """
        return pulumi.get(self, "frontend_port")

    @property
    @pulumi.getter(name="frontendProtocol")
    def frontend_protocol(self) -> pulumi.Output[str]:
        """
        The forwarding protocol. Valid values `tcp` and `udp`.
        """
        return pulumi.get(self, "frontend_protocol")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        The ID of Ddoscoo instance.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="realServers")
    def real_servers(self) -> pulumi.Output[Sequence[str]]:
        """
        List of source IP addresses.
        """
        return pulumi.get(self, "real_servers")

