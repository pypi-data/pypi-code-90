# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetInstancesInstanceResult',
    'GetZonesZoneResult',
]

@pulumi.output_type
class GetInstancesInstanceResult(dict):
    def __init__(__self__, *,
                 availability_zone: str,
                 charge_type: str,
                 creation_time: str,
                 description: str,
                 engine: str,
                 engine_version: str,
                 id: str,
                 instance_class: str,
                 instance_group_count: str,
                 instance_network_type: str,
                 region_id: str,
                 status: str):
        """
        :param str availability_zone: Instance availability zone.
        :param str charge_type: Billing method. Value options are `PostPaid` for  Pay-As-You-Go and `PrePaid` for yearly or monthly subscription.
        :param str creation_time: The time when you create an instance. The format is YYYY-MM-DDThh:mm:ssZ, such as 2011-05-30T12:11:4Z.
        :param str description: The description of an instance.
        :param str engine: Database engine type. Supported option is `gpdb`.
        :param str engine_version: Database engine version.
        :param str id: The instance id.
        :param str instance_class: The group type.
        :param str instance_group_count: The number of groups.
        :param str region_id: Region ID the instance belongs to.
        :param str status: Status of the instance.
        """
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "charge_type", charge_type)
        pulumi.set(__self__, "creation_time", creation_time)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "engine", engine)
        pulumi.set(__self__, "engine_version", engine_version)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "instance_class", instance_class)
        pulumi.set(__self__, "instance_group_count", instance_group_count)
        pulumi.set(__self__, "instance_network_type", instance_network_type)
        pulumi.set(__self__, "region_id", region_id)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        """
        Instance availability zone.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="chargeType")
    def charge_type(self) -> str:
        """
        Billing method. Value options are `PostPaid` for  Pay-As-You-Go and `PrePaid` for yearly or monthly subscription.
        """
        return pulumi.get(self, "charge_type")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        The time when you create an instance. The format is YYYY-MM-DDThh:mm:ssZ, such as 2011-05-30T12:11:4Z.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of an instance.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def engine(self) -> str:
        """
        Database engine type. Supported option is `gpdb`.
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> str:
        """
        Database engine version.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The instance id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceClass")
    def instance_class(self) -> str:
        """
        The group type.
        """
        return pulumi.get(self, "instance_class")

    @property
    @pulumi.getter(name="instanceGroupCount")
    def instance_group_count(self) -> str:
        """
        The number of groups.
        """
        return pulumi.get(self, "instance_group_count")

    @property
    @pulumi.getter(name="instanceNetworkType")
    def instance_network_type(self) -> str:
        return pulumi.get(self, "instance_network_type")

    @property
    @pulumi.getter(name="regionId")
    def region_id(self) -> str:
        """
        Region ID the instance belongs to.
        """
        return pulumi.get(self, "region_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the instance.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetZonesZoneResult(dict):
    def __init__(__self__, *,
                 id: str,
                 multi_zone_ids: Sequence[str]):
        """
        :param str id: ID of the zone.
        :param Sequence[str] multi_zone_ids: A list of zone ids in which the multi zone.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "multi_zone_ids", multi_zone_ids)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ID of the zone.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="multiZoneIds")
    def multi_zone_ids(self) -> Sequence[str]:
        """
        A list of zone ids in which the multi zone.
        """
        return pulumi.get(self, "multi_zone_ids")


