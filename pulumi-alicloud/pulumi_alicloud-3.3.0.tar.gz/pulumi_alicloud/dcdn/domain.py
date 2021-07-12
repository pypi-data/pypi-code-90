# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['DomainArgs', 'Domain']

@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 sources: pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]],
                 cert_name: Optional[pulumi.Input[str]] = None,
                 cert_type: Optional[pulumi.Input[str]] = None,
                 check_url: Optional[pulumi.Input[str]] = None,
                 force_set: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 security_token: Optional[pulumi.Input[str]] = None,
                 ssl_pri: Optional[pulumi.Input[str]] = None,
                 ssl_protocol: Optional[pulumi.Input[str]] = None,
                 ssl_pub: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 top_level_domain: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Domain resource.
        :param pulumi.Input[str] domain_name: The name of the accelerated domain.
        :param pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]] sources: The origin information.
        :param pulumi.Input[str] cert_name: Indicates the name of the certificate if the HTTPS protocol is enabled.
        :param pulumi.Input[str] cert_type: The type of the certificate. Valid values:
               `free`: a free certificate.
               `cas`: a certificate purchased from Alibaba Cloud SSL Certificates Service.
               `upload`: a user uploaded certificate.
        :param pulumi.Input[str] check_url: The URL that is used to test the accessibility of the origin.
        :param pulumi.Input[str] force_set: Specifies whether to check the certificate name for duplicates. If you set the value to 1, the system does not perform the check and overwrites the information of the existing certificate with the same name.
        :param pulumi.Input[str] resource_group_id: The ID of the resource group.
        :param pulumi.Input[str] scope: The acceleration region.
        :param pulumi.Input[str] ssl_pri: The private key. Specify this parameter only if you enable the SSL certificate.
        :param pulumi.Input[str] ssl_protocol: Indicates whether the SSL certificate is enabled. Valid values: `on` enabled, `off` disabled.
        :param pulumi.Input[str] ssl_pub: Indicates the public key of the certificate if the HTTPS protocol is enabled.
        :param pulumi.Input[str] status: The status of DCDN Domain. Valid values: `online`, `offline`. Default to `online`.
        :param pulumi.Input[str] top_level_domain: The top-level domain name.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "sources", sources)
        if cert_name is not None:
            pulumi.set(__self__, "cert_name", cert_name)
        if cert_type is not None:
            pulumi.set(__self__, "cert_type", cert_type)
        if check_url is not None:
            pulumi.set(__self__, "check_url", check_url)
        if force_set is not None:
            pulumi.set(__self__, "force_set", force_set)
        if resource_group_id is not None:
            pulumi.set(__self__, "resource_group_id", resource_group_id)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if security_token is not None:
            pulumi.set(__self__, "security_token", security_token)
        if ssl_pri is not None:
            pulumi.set(__self__, "ssl_pri", ssl_pri)
        if ssl_protocol is not None:
            pulumi.set(__self__, "ssl_protocol", ssl_protocol)
        if ssl_pub is not None:
            pulumi.set(__self__, "ssl_pub", ssl_pub)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if top_level_domain is not None:
            pulumi.set(__self__, "top_level_domain", top_level_domain)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The name of the accelerated domain.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]]:
        """
        The origin information.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]]):
        pulumi.set(self, "sources", value)

    @property
    @pulumi.getter(name="certName")
    def cert_name(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates the name of the certificate if the HTTPS protocol is enabled.
        """
        return pulumi.get(self, "cert_name")

    @cert_name.setter
    def cert_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert_name", value)

    @property
    @pulumi.getter(name="certType")
    def cert_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the certificate. Valid values:
        `free`: a free certificate.
        `cas`: a certificate purchased from Alibaba Cloud SSL Certificates Service.
        `upload`: a user uploaded certificate.
        """
        return pulumi.get(self, "cert_type")

    @cert_type.setter
    def cert_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert_type", value)

    @property
    @pulumi.getter(name="checkUrl")
    def check_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL that is used to test the accessibility of the origin.
        """
        return pulumi.get(self, "check_url")

    @check_url.setter
    def check_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "check_url", value)

    @property
    @pulumi.getter(name="forceSet")
    def force_set(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether to check the certificate name for duplicates. If you set the value to 1, the system does not perform the check and overwrites the information of the existing certificate with the same name.
        """
        return pulumi.get(self, "force_set")

    @force_set.setter
    def force_set(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "force_set", value)

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the resource group.
        """
        return pulumi.get(self, "resource_group_id")

    @resource_group_id.setter
    def resource_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_id", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The acceleration region.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="securityToken")
    def security_token(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "security_token")

    @security_token.setter
    def security_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_token", value)

    @property
    @pulumi.getter(name="sslPri")
    def ssl_pri(self) -> Optional[pulumi.Input[str]]:
        """
        The private key. Specify this parameter only if you enable the SSL certificate.
        """
        return pulumi.get(self, "ssl_pri")

    @ssl_pri.setter
    def ssl_pri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_pri", value)

    @property
    @pulumi.getter(name="sslProtocol")
    def ssl_protocol(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates whether the SSL certificate is enabled. Valid values: `on` enabled, `off` disabled.
        """
        return pulumi.get(self, "ssl_protocol")

    @ssl_protocol.setter
    def ssl_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_protocol", value)

    @property
    @pulumi.getter(name="sslPub")
    def ssl_pub(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates the public key of the certificate if the HTTPS protocol is enabled.
        """
        return pulumi.get(self, "ssl_pub")

    @ssl_pub.setter
    def ssl_pub(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_pub", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of DCDN Domain. Valid values: `online`, `offline`. Default to `online`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="topLevelDomain")
    def top_level_domain(self) -> Optional[pulumi.Input[str]]:
        """
        The top-level domain name.
        """
        return pulumi.get(self, "top_level_domain")

    @top_level_domain.setter
    def top_level_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "top_level_domain", value)


@pulumi.input_type
class _DomainState:
    def __init__(__self__, *,
                 cert_name: Optional[pulumi.Input[str]] = None,
                 cert_type: Optional[pulumi.Input[str]] = None,
                 check_url: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 force_set: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 security_token: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]]] = None,
                 ssl_pri: Optional[pulumi.Input[str]] = None,
                 ssl_protocol: Optional[pulumi.Input[str]] = None,
                 ssl_pub: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 top_level_domain: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Domain resources.
        :param pulumi.Input[str] cert_name: Indicates the name of the certificate if the HTTPS protocol is enabled.
        :param pulumi.Input[str] cert_type: The type of the certificate. Valid values:
               `free`: a free certificate.
               `cas`: a certificate purchased from Alibaba Cloud SSL Certificates Service.
               `upload`: a user uploaded certificate.
        :param pulumi.Input[str] check_url: The URL that is used to test the accessibility of the origin.
        :param pulumi.Input[str] domain_name: The name of the accelerated domain.
        :param pulumi.Input[str] force_set: Specifies whether to check the certificate name for duplicates. If you set the value to 1, the system does not perform the check and overwrites the information of the existing certificate with the same name.
        :param pulumi.Input[str] resource_group_id: The ID of the resource group.
        :param pulumi.Input[str] scope: The acceleration region.
        :param pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]] sources: The origin information.
        :param pulumi.Input[str] ssl_pri: The private key. Specify this parameter only if you enable the SSL certificate.
        :param pulumi.Input[str] ssl_protocol: Indicates whether the SSL certificate is enabled. Valid values: `on` enabled, `off` disabled.
        :param pulumi.Input[str] ssl_pub: Indicates the public key of the certificate if the HTTPS protocol is enabled.
        :param pulumi.Input[str] status: The status of DCDN Domain. Valid values: `online`, `offline`. Default to `online`.
        :param pulumi.Input[str] top_level_domain: The top-level domain name.
        """
        if cert_name is not None:
            pulumi.set(__self__, "cert_name", cert_name)
        if cert_type is not None:
            pulumi.set(__self__, "cert_type", cert_type)
        if check_url is not None:
            pulumi.set(__self__, "check_url", check_url)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if force_set is not None:
            pulumi.set(__self__, "force_set", force_set)
        if resource_group_id is not None:
            pulumi.set(__self__, "resource_group_id", resource_group_id)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if security_token is not None:
            pulumi.set(__self__, "security_token", security_token)
        if sources is not None:
            pulumi.set(__self__, "sources", sources)
        if ssl_pri is not None:
            pulumi.set(__self__, "ssl_pri", ssl_pri)
        if ssl_protocol is not None:
            pulumi.set(__self__, "ssl_protocol", ssl_protocol)
        if ssl_pub is not None:
            pulumi.set(__self__, "ssl_pub", ssl_pub)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if top_level_domain is not None:
            pulumi.set(__self__, "top_level_domain", top_level_domain)

    @property
    @pulumi.getter(name="certName")
    def cert_name(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates the name of the certificate if the HTTPS protocol is enabled.
        """
        return pulumi.get(self, "cert_name")

    @cert_name.setter
    def cert_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert_name", value)

    @property
    @pulumi.getter(name="certType")
    def cert_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the certificate. Valid values:
        `free`: a free certificate.
        `cas`: a certificate purchased from Alibaba Cloud SSL Certificates Service.
        `upload`: a user uploaded certificate.
        """
        return pulumi.get(self, "cert_type")

    @cert_type.setter
    def cert_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert_type", value)

    @property
    @pulumi.getter(name="checkUrl")
    def check_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL that is used to test the accessibility of the origin.
        """
        return pulumi.get(self, "check_url")

    @check_url.setter
    def check_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "check_url", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the accelerated domain.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="forceSet")
    def force_set(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether to check the certificate name for duplicates. If you set the value to 1, the system does not perform the check and overwrites the information of the existing certificate with the same name.
        """
        return pulumi.get(self, "force_set")

    @force_set.setter
    def force_set(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "force_set", value)

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the resource group.
        """
        return pulumi.get(self, "resource_group_id")

    @resource_group_id.setter
    def resource_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_id", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        The acceleration region.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="securityToken")
    def security_token(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "security_token")

    @security_token.setter
    def security_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_token", value)

    @property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]]]:
        """
        The origin information.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]]]):
        pulumi.set(self, "sources", value)

    @property
    @pulumi.getter(name="sslPri")
    def ssl_pri(self) -> Optional[pulumi.Input[str]]:
        """
        The private key. Specify this parameter only if you enable the SSL certificate.
        """
        return pulumi.get(self, "ssl_pri")

    @ssl_pri.setter
    def ssl_pri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_pri", value)

    @property
    @pulumi.getter(name="sslProtocol")
    def ssl_protocol(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates whether the SSL certificate is enabled. Valid values: `on` enabled, `off` disabled.
        """
        return pulumi.get(self, "ssl_protocol")

    @ssl_protocol.setter
    def ssl_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_protocol", value)

    @property
    @pulumi.getter(name="sslPub")
    def ssl_pub(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates the public key of the certificate if the HTTPS protocol is enabled.
        """
        return pulumi.get(self, "ssl_pub")

    @ssl_pub.setter
    def ssl_pub(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_pub", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of DCDN Domain. Valid values: `online`, `offline`. Default to `online`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="topLevelDomain")
    def top_level_domain(self) -> Optional[pulumi.Input[str]]:
        """
        The top-level domain name.
        """
        return pulumi.get(self, "top_level_domain")

    @top_level_domain.setter
    def top_level_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "top_level_domain", value)


class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cert_name: Optional[pulumi.Input[str]] = None,
                 cert_type: Optional[pulumi.Input[str]] = None,
                 check_url: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 force_set: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 security_token: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainSourceArgs']]]]] = None,
                 ssl_pri: Optional[pulumi.Input[str]] = None,
                 ssl_protocol: Optional[pulumi.Input[str]] = None,
                 ssl_pub: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 top_level_domain: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        You can use DCDN to improve the overall performance of your website and accelerate content delivery to improve user experience. For information about Alicloud DCDN Domain and how to use it, see [What is Resource Alicloud DCDN Domain](https://www.alibabacloud.com/help/en/doc-detail/130628.htm).

        > **NOTE:** Available in v1.94.0+.

        > **NOTE:** You must activate the Dynamic Route for CDN (DCDN) service before you create an accelerated domain.

        > **NOTE:** Make sure that you have obtained an Internet content provider (ICP) filling for the accelerated domain.

        > **NOTE:** If the origin content is not saved on Alibaba Cloud, the content must be reviewed by Alibaba Cloud. The review will be completed by the next working day after you submit the application.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.dcdn.Domain("example",
            domain_name="example.com",
            scope="overseas",
            sources=[alicloud.dcdn.DomainSourceArgs(
                content="1.1.1.1",
                port=80,
                priority="20",
                type="ipaddr",
            )])
        ```

        ## Import

        DCDN Domain can be imported using the id or DCDN Domain name, e.g.

        ```sh
         $ pulumi import alicloud:dcdn/domain:Domain example example.com
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cert_name: Indicates the name of the certificate if the HTTPS protocol is enabled.
        :param pulumi.Input[str] cert_type: The type of the certificate. Valid values:
               `free`: a free certificate.
               `cas`: a certificate purchased from Alibaba Cloud SSL Certificates Service.
               `upload`: a user uploaded certificate.
        :param pulumi.Input[str] check_url: The URL that is used to test the accessibility of the origin.
        :param pulumi.Input[str] domain_name: The name of the accelerated domain.
        :param pulumi.Input[str] force_set: Specifies whether to check the certificate name for duplicates. If you set the value to 1, the system does not perform the check and overwrites the information of the existing certificate with the same name.
        :param pulumi.Input[str] resource_group_id: The ID of the resource group.
        :param pulumi.Input[str] scope: The acceleration region.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainSourceArgs']]]] sources: The origin information.
        :param pulumi.Input[str] ssl_pri: The private key. Specify this parameter only if you enable the SSL certificate.
        :param pulumi.Input[str] ssl_protocol: Indicates whether the SSL certificate is enabled. Valid values: `on` enabled, `off` disabled.
        :param pulumi.Input[str] ssl_pub: Indicates the public key of the certificate if the HTTPS protocol is enabled.
        :param pulumi.Input[str] status: The status of DCDN Domain. Valid values: `online`, `offline`. Default to `online`.
        :param pulumi.Input[str] top_level_domain: The top-level domain name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        You can use DCDN to improve the overall performance of your website and accelerate content delivery to improve user experience. For information about Alicloud DCDN Domain and how to use it, see [What is Resource Alicloud DCDN Domain](https://www.alibabacloud.com/help/en/doc-detail/130628.htm).

        > **NOTE:** Available in v1.94.0+.

        > **NOTE:** You must activate the Dynamic Route for CDN (DCDN) service before you create an accelerated domain.

        > **NOTE:** Make sure that you have obtained an Internet content provider (ICP) filling for the accelerated domain.

        > **NOTE:** If the origin content is not saved on Alibaba Cloud, the content must be reviewed by Alibaba Cloud. The review will be completed by the next working day after you submit the application.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.dcdn.Domain("example",
            domain_name="example.com",
            scope="overseas",
            sources=[alicloud.dcdn.DomainSourceArgs(
                content="1.1.1.1",
                port=80,
                priority="20",
                type="ipaddr",
            )])
        ```

        ## Import

        DCDN Domain can be imported using the id or DCDN Domain name, e.g.

        ```sh
         $ pulumi import alicloud:dcdn/domain:Domain example example.com
        ```

        :param str resource_name: The name of the resource.
        :param DomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cert_name: Optional[pulumi.Input[str]] = None,
                 cert_type: Optional[pulumi.Input[str]] = None,
                 check_url: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 force_set: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 security_token: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainSourceArgs']]]]] = None,
                 ssl_pri: Optional[pulumi.Input[str]] = None,
                 ssl_protocol: Optional[pulumi.Input[str]] = None,
                 ssl_pub: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 top_level_domain: Optional[pulumi.Input[str]] = None,
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
            __props__ = DomainArgs.__new__(DomainArgs)

            __props__.__dict__["cert_name"] = cert_name
            __props__.__dict__["cert_type"] = cert_type
            __props__.__dict__["check_url"] = check_url
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["force_set"] = force_set
            __props__.__dict__["resource_group_id"] = resource_group_id
            __props__.__dict__["scope"] = scope
            __props__.__dict__["security_token"] = security_token
            if sources is None and not opts.urn:
                raise TypeError("Missing required property 'sources'")
            __props__.__dict__["sources"] = sources
            __props__.__dict__["ssl_pri"] = ssl_pri
            __props__.__dict__["ssl_protocol"] = ssl_protocol
            __props__.__dict__["ssl_pub"] = ssl_pub
            __props__.__dict__["status"] = status
            __props__.__dict__["top_level_domain"] = top_level_domain
        super(Domain, __self__).__init__(
            'alicloud:dcdn/domain:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cert_name: Optional[pulumi.Input[str]] = None,
            cert_type: Optional[pulumi.Input[str]] = None,
            check_url: Optional[pulumi.Input[str]] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            force_set: Optional[pulumi.Input[str]] = None,
            resource_group_id: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None,
            security_token: Optional[pulumi.Input[str]] = None,
            sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainSourceArgs']]]]] = None,
            ssl_pri: Optional[pulumi.Input[str]] = None,
            ssl_protocol: Optional[pulumi.Input[str]] = None,
            ssl_pub: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            top_level_domain: Optional[pulumi.Input[str]] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cert_name: Indicates the name of the certificate if the HTTPS protocol is enabled.
        :param pulumi.Input[str] cert_type: The type of the certificate. Valid values:
               `free`: a free certificate.
               `cas`: a certificate purchased from Alibaba Cloud SSL Certificates Service.
               `upload`: a user uploaded certificate.
        :param pulumi.Input[str] check_url: The URL that is used to test the accessibility of the origin.
        :param pulumi.Input[str] domain_name: The name of the accelerated domain.
        :param pulumi.Input[str] force_set: Specifies whether to check the certificate name for duplicates. If you set the value to 1, the system does not perform the check and overwrites the information of the existing certificate with the same name.
        :param pulumi.Input[str] resource_group_id: The ID of the resource group.
        :param pulumi.Input[str] scope: The acceleration region.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainSourceArgs']]]] sources: The origin information.
        :param pulumi.Input[str] ssl_pri: The private key. Specify this parameter only if you enable the SSL certificate.
        :param pulumi.Input[str] ssl_protocol: Indicates whether the SSL certificate is enabled. Valid values: `on` enabled, `off` disabled.
        :param pulumi.Input[str] ssl_pub: Indicates the public key of the certificate if the HTTPS protocol is enabled.
        :param pulumi.Input[str] status: The status of DCDN Domain. Valid values: `online`, `offline`. Default to `online`.
        :param pulumi.Input[str] top_level_domain: The top-level domain name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainState.__new__(_DomainState)

        __props__.__dict__["cert_name"] = cert_name
        __props__.__dict__["cert_type"] = cert_type
        __props__.__dict__["check_url"] = check_url
        __props__.__dict__["domain_name"] = domain_name
        __props__.__dict__["force_set"] = force_set
        __props__.__dict__["resource_group_id"] = resource_group_id
        __props__.__dict__["scope"] = scope
        __props__.__dict__["security_token"] = security_token
        __props__.__dict__["sources"] = sources
        __props__.__dict__["ssl_pri"] = ssl_pri
        __props__.__dict__["ssl_protocol"] = ssl_protocol
        __props__.__dict__["ssl_pub"] = ssl_pub
        __props__.__dict__["status"] = status
        __props__.__dict__["top_level_domain"] = top_level_domain
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certName")
    def cert_name(self) -> pulumi.Output[str]:
        """
        Indicates the name of the certificate if the HTTPS protocol is enabled.
        """
        return pulumi.get(self, "cert_name")

    @property
    @pulumi.getter(name="certType")
    def cert_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the certificate. Valid values:
        `free`: a free certificate.
        `cas`: a certificate purchased from Alibaba Cloud SSL Certificates Service.
        `upload`: a user uploaded certificate.
        """
        return pulumi.get(self, "cert_type")

    @property
    @pulumi.getter(name="checkUrl")
    def check_url(self) -> pulumi.Output[Optional[str]]:
        """
        The URL that is used to test the accessibility of the origin.
        """
        return pulumi.get(self, "check_url")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The name of the accelerated domain.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="forceSet")
    def force_set(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies whether to check the certificate name for duplicates. If you set the value to 1, the system does not perform the check and overwrites the information of the existing certificate with the same name.
        """
        return pulumi.get(self, "force_set")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the resource group.
        """
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        The acceleration region.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="securityToken")
    def security_token(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "security_token")

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Sequence['outputs.DomainSource']]:
        """
        The origin information.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter(name="sslPri")
    def ssl_pri(self) -> pulumi.Output[Optional[str]]:
        """
        The private key. Specify this parameter only if you enable the SSL certificate.
        """
        return pulumi.get(self, "ssl_pri")

    @property
    @pulumi.getter(name="sslProtocol")
    def ssl_protocol(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates whether the SSL certificate is enabled. Valid values: `on` enabled, `off` disabled.
        """
        return pulumi.get(self, "ssl_protocol")

    @property
    @pulumi.getter(name="sslPub")
    def ssl_pub(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates the public key of the certificate if the HTTPS protocol is enabled.
        """
        return pulumi.get(self, "ssl_pub")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of DCDN Domain. Valid values: `online`, `offline`. Default to `online`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="topLevelDomain")
    def top_level_domain(self) -> pulumi.Output[Optional[str]]:
        """
        The top-level domain name.
        """
        return pulumi.get(self, "top_level_domain")

