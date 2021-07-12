# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['QueueArgs', 'Queue']

@pulumi.input_type
class QueueArgs:
    def __init__(__self__, *,
                 delay_seconds: Optional[pulumi.Input[int]] = None,
                 maximum_message_size: Optional[pulumi.Input[int]] = None,
                 message_retention_period: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 polling_wait_seconds: Optional[pulumi.Input[int]] = None,
                 visibility_timeout: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Queue resource.
        :param pulumi.Input[int] delay_seconds: This attribute defines the length of time, in seconds, after which every message sent to the queue is dequeued. Valid value range: 0-604800 seconds, i.e., 0 to 7 days. Default value to 0.
        :param pulumi.Input[int] maximum_message_size: This indicates the maximum length, in bytes, of any message body sent to the queue. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.
        :param pulumi.Input[int] message_retention_period: Messages are deleted from the queue after a specified length of time, whether they have been activated or not. This attribute defines the viability period, in seconds, for every message in the queue. Valid value range: 60-604800 seconds, i.e., 1 minutes to 7 days. Default value to 345600.
        :param pulumi.Input[str] name: Two queues on a single account in the same region cannot have the same name. A queue name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters .
        :param pulumi.Input[int] polling_wait_seconds: Long polling is measured in seconds. When this attribute is set to 0, long polling is disabled. When it is not set to 0, long polling is enabled and message dequeue requests will be processed only when valid messages are received or when long polling times out. Valid value range: 0-30 seconds. Default value to 0.
        :param pulumi.Input[int] visibility_timeout: The VisibilityTimeout attribute of the queue. A dequeued messages will change from active (visible) status to inactive (invisible) status, and this attribute defines the length of time, in seconds, that messages remain invisible. Messages return to active status after the set period. Valid value range: 1-43200 seconds, i.e., 1 seconds to 12 hours. Default value to 30.
        """
        if delay_seconds is not None:
            pulumi.set(__self__, "delay_seconds", delay_seconds)
        if maximum_message_size is not None:
            pulumi.set(__self__, "maximum_message_size", maximum_message_size)
        if message_retention_period is not None:
            pulumi.set(__self__, "message_retention_period", message_retention_period)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if polling_wait_seconds is not None:
            pulumi.set(__self__, "polling_wait_seconds", polling_wait_seconds)
        if visibility_timeout is not None:
            pulumi.set(__self__, "visibility_timeout", visibility_timeout)

    @property
    @pulumi.getter(name="delaySeconds")
    def delay_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        This attribute defines the length of time, in seconds, after which every message sent to the queue is dequeued. Valid value range: 0-604800 seconds, i.e., 0 to 7 days. Default value to 0.
        """
        return pulumi.get(self, "delay_seconds")

    @delay_seconds.setter
    def delay_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "delay_seconds", value)

    @property
    @pulumi.getter(name="maximumMessageSize")
    def maximum_message_size(self) -> Optional[pulumi.Input[int]]:
        """
        This indicates the maximum length, in bytes, of any message body sent to the queue. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.
        """
        return pulumi.get(self, "maximum_message_size")

    @maximum_message_size.setter
    def maximum_message_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "maximum_message_size", value)

    @property
    @pulumi.getter(name="messageRetentionPeriod")
    def message_retention_period(self) -> Optional[pulumi.Input[int]]:
        """
        Messages are deleted from the queue after a specified length of time, whether they have been activated or not. This attribute defines the viability period, in seconds, for every message in the queue. Valid value range: 60-604800 seconds, i.e., 1 minutes to 7 days. Default value to 345600.
        """
        return pulumi.get(self, "message_retention_period")

    @message_retention_period.setter
    def message_retention_period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "message_retention_period", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Two queues on a single account in the same region cannot have the same name. A queue name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters .
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="pollingWaitSeconds")
    def polling_wait_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Long polling is measured in seconds. When this attribute is set to 0, long polling is disabled. When it is not set to 0, long polling is enabled and message dequeue requests will be processed only when valid messages are received or when long polling times out. Valid value range: 0-30 seconds. Default value to 0.
        """
        return pulumi.get(self, "polling_wait_seconds")

    @polling_wait_seconds.setter
    def polling_wait_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "polling_wait_seconds", value)

    @property
    @pulumi.getter(name="visibilityTimeout")
    def visibility_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        The VisibilityTimeout attribute of the queue. A dequeued messages will change from active (visible) status to inactive (invisible) status, and this attribute defines the length of time, in seconds, that messages remain invisible. Messages return to active status after the set period. Valid value range: 1-43200 seconds, i.e., 1 seconds to 12 hours. Default value to 30.
        """
        return pulumi.get(self, "visibility_timeout")

    @visibility_timeout.setter
    def visibility_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "visibility_timeout", value)


@pulumi.input_type
class _QueueState:
    def __init__(__self__, *,
                 delay_seconds: Optional[pulumi.Input[int]] = None,
                 maximum_message_size: Optional[pulumi.Input[int]] = None,
                 message_retention_period: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 polling_wait_seconds: Optional[pulumi.Input[int]] = None,
                 visibility_timeout: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Queue resources.
        :param pulumi.Input[int] delay_seconds: This attribute defines the length of time, in seconds, after which every message sent to the queue is dequeued. Valid value range: 0-604800 seconds, i.e., 0 to 7 days. Default value to 0.
        :param pulumi.Input[int] maximum_message_size: This indicates the maximum length, in bytes, of any message body sent to the queue. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.
        :param pulumi.Input[int] message_retention_period: Messages are deleted from the queue after a specified length of time, whether they have been activated or not. This attribute defines the viability period, in seconds, for every message in the queue. Valid value range: 60-604800 seconds, i.e., 1 minutes to 7 days. Default value to 345600.
        :param pulumi.Input[str] name: Two queues on a single account in the same region cannot have the same name. A queue name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters .
        :param pulumi.Input[int] polling_wait_seconds: Long polling is measured in seconds. When this attribute is set to 0, long polling is disabled. When it is not set to 0, long polling is enabled and message dequeue requests will be processed only when valid messages are received or when long polling times out. Valid value range: 0-30 seconds. Default value to 0.
        :param pulumi.Input[int] visibility_timeout: The VisibilityTimeout attribute of the queue. A dequeued messages will change from active (visible) status to inactive (invisible) status, and this attribute defines the length of time, in seconds, that messages remain invisible. Messages return to active status after the set period. Valid value range: 1-43200 seconds, i.e., 1 seconds to 12 hours. Default value to 30.
        """
        if delay_seconds is not None:
            pulumi.set(__self__, "delay_seconds", delay_seconds)
        if maximum_message_size is not None:
            pulumi.set(__self__, "maximum_message_size", maximum_message_size)
        if message_retention_period is not None:
            pulumi.set(__self__, "message_retention_period", message_retention_period)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if polling_wait_seconds is not None:
            pulumi.set(__self__, "polling_wait_seconds", polling_wait_seconds)
        if visibility_timeout is not None:
            pulumi.set(__self__, "visibility_timeout", visibility_timeout)

    @property
    @pulumi.getter(name="delaySeconds")
    def delay_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        This attribute defines the length of time, in seconds, after which every message sent to the queue is dequeued. Valid value range: 0-604800 seconds, i.e., 0 to 7 days. Default value to 0.
        """
        return pulumi.get(self, "delay_seconds")

    @delay_seconds.setter
    def delay_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "delay_seconds", value)

    @property
    @pulumi.getter(name="maximumMessageSize")
    def maximum_message_size(self) -> Optional[pulumi.Input[int]]:
        """
        This indicates the maximum length, in bytes, of any message body sent to the queue. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.
        """
        return pulumi.get(self, "maximum_message_size")

    @maximum_message_size.setter
    def maximum_message_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "maximum_message_size", value)

    @property
    @pulumi.getter(name="messageRetentionPeriod")
    def message_retention_period(self) -> Optional[pulumi.Input[int]]:
        """
        Messages are deleted from the queue after a specified length of time, whether they have been activated or not. This attribute defines the viability period, in seconds, for every message in the queue. Valid value range: 60-604800 seconds, i.e., 1 minutes to 7 days. Default value to 345600.
        """
        return pulumi.get(self, "message_retention_period")

    @message_retention_period.setter
    def message_retention_period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "message_retention_period", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Two queues on a single account in the same region cannot have the same name. A queue name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters .
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="pollingWaitSeconds")
    def polling_wait_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Long polling is measured in seconds. When this attribute is set to 0, long polling is disabled. When it is not set to 0, long polling is enabled and message dequeue requests will be processed only when valid messages are received or when long polling times out. Valid value range: 0-30 seconds. Default value to 0.
        """
        return pulumi.get(self, "polling_wait_seconds")

    @polling_wait_seconds.setter
    def polling_wait_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "polling_wait_seconds", value)

    @property
    @pulumi.getter(name="visibilityTimeout")
    def visibility_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        The VisibilityTimeout attribute of the queue. A dequeued messages will change from active (visible) status to inactive (invisible) status, and this attribute defines the length of time, in seconds, that messages remain invisible. Messages return to active status after the set period. Valid value range: 1-43200 seconds, i.e., 1 seconds to 12 hours. Default value to 30.
        """
        return pulumi.get(self, "visibility_timeout")

    @visibility_timeout.setter
    def visibility_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "visibility_timeout", value)


class Queue(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delay_seconds: Optional[pulumi.Input[int]] = None,
                 maximum_message_size: Optional[pulumi.Input[int]] = None,
                 message_retention_period: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 polling_wait_seconds: Optional[pulumi.Input[int]] = None,
                 visibility_timeout: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        ## Import

        MNS QUEUE can be imported using the id or name, e.g.

        ```sh
         $ pulumi import alicloud:mns/queue:Queue queue queuename
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] delay_seconds: This attribute defines the length of time, in seconds, after which every message sent to the queue is dequeued. Valid value range: 0-604800 seconds, i.e., 0 to 7 days. Default value to 0.
        :param pulumi.Input[int] maximum_message_size: This indicates the maximum length, in bytes, of any message body sent to the queue. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.
        :param pulumi.Input[int] message_retention_period: Messages are deleted from the queue after a specified length of time, whether they have been activated or not. This attribute defines the viability period, in seconds, for every message in the queue. Valid value range: 60-604800 seconds, i.e., 1 minutes to 7 days. Default value to 345600.
        :param pulumi.Input[str] name: Two queues on a single account in the same region cannot have the same name. A queue name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters .
        :param pulumi.Input[int] polling_wait_seconds: Long polling is measured in seconds. When this attribute is set to 0, long polling is disabled. When it is not set to 0, long polling is enabled and message dequeue requests will be processed only when valid messages are received or when long polling times out. Valid value range: 0-30 seconds. Default value to 0.
        :param pulumi.Input[int] visibility_timeout: The VisibilityTimeout attribute of the queue. A dequeued messages will change from active (visible) status to inactive (invisible) status, and this attribute defines the length of time, in seconds, that messages remain invisible. Messages return to active status after the set period. Valid value range: 1-43200 seconds, i.e., 1 seconds to 12 hours. Default value to 30.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[QueueArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        MNS QUEUE can be imported using the id or name, e.g.

        ```sh
         $ pulumi import alicloud:mns/queue:Queue queue queuename
        ```

        :param str resource_name: The name of the resource.
        :param QueueArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(QueueArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delay_seconds: Optional[pulumi.Input[int]] = None,
                 maximum_message_size: Optional[pulumi.Input[int]] = None,
                 message_retention_period: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 polling_wait_seconds: Optional[pulumi.Input[int]] = None,
                 visibility_timeout: Optional[pulumi.Input[int]] = None,
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
            __props__ = QueueArgs.__new__(QueueArgs)

            __props__.__dict__["delay_seconds"] = delay_seconds
            __props__.__dict__["maximum_message_size"] = maximum_message_size
            __props__.__dict__["message_retention_period"] = message_retention_period
            __props__.__dict__["name"] = name
            __props__.__dict__["polling_wait_seconds"] = polling_wait_seconds
            __props__.__dict__["visibility_timeout"] = visibility_timeout
        super(Queue, __self__).__init__(
            'alicloud:mns/queue:Queue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            delay_seconds: Optional[pulumi.Input[int]] = None,
            maximum_message_size: Optional[pulumi.Input[int]] = None,
            message_retention_period: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            polling_wait_seconds: Optional[pulumi.Input[int]] = None,
            visibility_timeout: Optional[pulumi.Input[int]] = None) -> 'Queue':
        """
        Get an existing Queue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] delay_seconds: This attribute defines the length of time, in seconds, after which every message sent to the queue is dequeued. Valid value range: 0-604800 seconds, i.e., 0 to 7 days. Default value to 0.
        :param pulumi.Input[int] maximum_message_size: This indicates the maximum length, in bytes, of any message body sent to the queue. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.
        :param pulumi.Input[int] message_retention_period: Messages are deleted from the queue after a specified length of time, whether they have been activated or not. This attribute defines the viability period, in seconds, for every message in the queue. Valid value range: 60-604800 seconds, i.e., 1 minutes to 7 days. Default value to 345600.
        :param pulumi.Input[str] name: Two queues on a single account in the same region cannot have the same name. A queue name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters .
        :param pulumi.Input[int] polling_wait_seconds: Long polling is measured in seconds. When this attribute is set to 0, long polling is disabled. When it is not set to 0, long polling is enabled and message dequeue requests will be processed only when valid messages are received or when long polling times out. Valid value range: 0-30 seconds. Default value to 0.
        :param pulumi.Input[int] visibility_timeout: The VisibilityTimeout attribute of the queue. A dequeued messages will change from active (visible) status to inactive (invisible) status, and this attribute defines the length of time, in seconds, that messages remain invisible. Messages return to active status after the set period. Valid value range: 1-43200 seconds, i.e., 1 seconds to 12 hours. Default value to 30.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _QueueState.__new__(_QueueState)

        __props__.__dict__["delay_seconds"] = delay_seconds
        __props__.__dict__["maximum_message_size"] = maximum_message_size
        __props__.__dict__["message_retention_period"] = message_retention_period
        __props__.__dict__["name"] = name
        __props__.__dict__["polling_wait_seconds"] = polling_wait_seconds
        __props__.__dict__["visibility_timeout"] = visibility_timeout
        return Queue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="delaySeconds")
    def delay_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        This attribute defines the length of time, in seconds, after which every message sent to the queue is dequeued. Valid value range: 0-604800 seconds, i.e., 0 to 7 days. Default value to 0.
        """
        return pulumi.get(self, "delay_seconds")

    @property
    @pulumi.getter(name="maximumMessageSize")
    def maximum_message_size(self) -> pulumi.Output[Optional[int]]:
        """
        This indicates the maximum length, in bytes, of any message body sent to the queue. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.
        """
        return pulumi.get(self, "maximum_message_size")

    @property
    @pulumi.getter(name="messageRetentionPeriod")
    def message_retention_period(self) -> pulumi.Output[Optional[int]]:
        """
        Messages are deleted from the queue after a specified length of time, whether they have been activated or not. This attribute defines the viability period, in seconds, for every message in the queue. Valid value range: 60-604800 seconds, i.e., 1 minutes to 7 days. Default value to 345600.
        """
        return pulumi.get(self, "message_retention_period")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Two queues on a single account in the same region cannot have the same name. A queue name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters .
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pollingWaitSeconds")
    def polling_wait_seconds(self) -> pulumi.Output[Optional[int]]:
        """
        Long polling is measured in seconds. When this attribute is set to 0, long polling is disabled. When it is not set to 0, long polling is enabled and message dequeue requests will be processed only when valid messages are received or when long polling times out. Valid value range: 0-30 seconds. Default value to 0.
        """
        return pulumi.get(self, "polling_wait_seconds")

    @property
    @pulumi.getter(name="visibilityTimeout")
    def visibility_timeout(self) -> pulumi.Output[Optional[int]]:
        """
        The VisibilityTimeout attribute of the queue. A dequeued messages will change from active (visible) status to inactive (invisible) status, and this attribute defines the length of time, in seconds, that messages remain invisible. Messages return to active status after the set period. Valid value range: 1-43200 seconds, i.e., 1 seconds to 12 hours. Default value to 30.
        """
        return pulumi.get(self, "visibility_timeout")

