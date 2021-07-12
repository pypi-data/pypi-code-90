# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetKeyPairsResult',
    'AwaitableGetKeyPairsResult',
    'get_key_pairs',
]

@pulumi.output_type
class GetKeyPairsResult:
    """
    A collection of values returned by getKeyPairs.
    """
    def __init__(__self__, finger_print=None, id=None, ids=None, key_pairs=None, name_regex=None, names=None, output_file=None, pairs=None, resource_group_id=None, tags=None):
        if finger_print and not isinstance(finger_print, str):
            raise TypeError("Expected argument 'finger_print' to be a str")
        pulumi.set(__self__, "finger_print", finger_print)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if key_pairs and not isinstance(key_pairs, list):
            raise TypeError("Expected argument 'key_pairs' to be a list")
        if key_pairs is not None:
            warnings.warn("""Field 'key_pairs' has been deprecated from provider version 1.121.0. New field 'pairs' instead.""", DeprecationWarning)
            pulumi.log.warn("""key_pairs is deprecated: Field 'key_pairs' has been deprecated from provider version 1.121.0. New field 'pairs' instead.""")

        pulumi.set(__self__, "key_pairs", key_pairs)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if pairs and not isinstance(pairs, list):
            raise TypeError("Expected argument 'pairs' to be a list")
        pulumi.set(__self__, "pairs", pairs)
        if resource_group_id and not isinstance(resource_group_id, str):
            raise TypeError("Expected argument 'resource_group_id' to be a str")
        pulumi.set(__self__, "resource_group_id", resource_group_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="fingerPrint")
    def finger_print(self) -> Optional[str]:
        """
        Finger print of the key pair.
        """
        return pulumi.get(self, "finger_print")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="keyPairs")
    def key_pairs(self) -> Sequence['outputs.GetKeyPairsKeyPairResult']:
        """
        A list of key pairs. Each element contains the following attributes:
        """
        return pulumi.get(self, "key_pairs")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of key pair names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def pairs(self) -> Sequence['outputs.GetKeyPairsPairResult']:
        return pulumi.get(self, "pairs")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[str]:
        """
        The Id of resource group.
        """
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Any]]:
        """
        (Optional, Available in v1.66.0+) A mapping of tags to assign to the resource.
        """
        return pulumi.get(self, "tags")


class AwaitableGetKeyPairsResult(GetKeyPairsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeyPairsResult(
            finger_print=self.finger_print,
            id=self.id,
            ids=self.ids,
            key_pairs=self.key_pairs,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            pairs=self.pairs,
            resource_group_id=self.resource_group_id,
            tags=self.tags)


def get_key_pairs(finger_print: Optional[str] = None,
                  ids: Optional[Sequence[str]] = None,
                  name_regex: Optional[str] = None,
                  output_file: Optional[str] = None,
                  resource_group_id: Optional[str] = None,
                  tags: Optional[Mapping[str, Any]] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeyPairsResult:
    """
    Use this data source to access information about an existing resource.

    :param str finger_print: A finger print used to retrieve specified key pair.
    :param Sequence[str] ids: A list of key pair IDs.
    :param str name_regex: A regex string to apply to the resulting key pairs.
    :param str resource_group_id: The Id of resource group which the key pair belongs.
    :param Mapping[str, Any] tags: A mapping of tags to assign to the resource.
    """
    __args__ = dict()
    __args__['fingerPrint'] = finger_print
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['resourceGroupId'] = resource_group_id
    __args__['tags'] = tags
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:ecs/getKeyPairs:getKeyPairs', __args__, opts=opts, typ=GetKeyPairsResult).value

    return AwaitableGetKeyPairsResult(
        finger_print=__ret__.finger_print,
        id=__ret__.id,
        ids=__ret__.ids,
        key_pairs=__ret__.key_pairs,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        pairs=__ret__.pairs,
        resource_group_id=__ret__.resource_group_id,
        tags=__ret__.tags)
