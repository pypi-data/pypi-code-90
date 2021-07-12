# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.apigateway.v1",
    manifest={
        "Api",
        "ApiConfig",
        "Gateway",
        "ListGatewaysRequest",
        "ListGatewaysResponse",
        "GetGatewayRequest",
        "CreateGatewayRequest",
        "UpdateGatewayRequest",
        "DeleteGatewayRequest",
        "ListApisRequest",
        "ListApisResponse",
        "GetApiRequest",
        "CreateApiRequest",
        "UpdateApiRequest",
        "DeleteApiRequest",
        "ListApiConfigsRequest",
        "ListApiConfigsResponse",
        "GetApiConfigRequest",
        "CreateApiConfigRequest",
        "UpdateApiConfigRequest",
        "DeleteApiConfigRequest",
        "OperationMetadata",
    },
)


class Api(proto.Message):
    r"""An API that can be served by one or more Gateways.
    Attributes:
        name (str):
            Output only. Resource name of the API.
            Format:
            projects/{project}/locations/global/apis/{api}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Created time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Updated time.
        labels (Sequence[google.cloud.apigateway_v1.types.Api.LabelsEntry]):
            Optional. Resource labels to represent user-
            rovided metadata. Refer to cloud documentation
            on labels for more details.
            https://cloud.google.com/compute/docs/labeling-
            resources
        display_name (str):
            Optional. Display name.
        managed_service (str):
            Optional. Immutable. The name of a Google
            Managed Service (
            https://cloud.google.com/service-
            infrastructure/docs/glossary#managed). If not
            specified, a new Service will automatically be
            created in the same project as this API.
        state (google.cloud.apigateway_v1.types.Api.State):
            Output only. State of the API.
    """

    class State(proto.Enum):
        r"""All the possible API states."""
        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        FAILED = 3
        DELETING = 4
        UPDATING = 5

    name = proto.Field(proto.STRING, number=1,)
    create_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    labels = proto.MapField(proto.STRING, proto.STRING, number=4,)
    display_name = proto.Field(proto.STRING, number=5,)
    managed_service = proto.Field(proto.STRING, number=7,)
    state = proto.Field(proto.ENUM, number=12, enum=State,)


class ApiConfig(proto.Message):
    r"""An API Configuration is a combination of settings for both
    the Managed Service and Gateways serving this API Config.

    Attributes:
        name (str):
            Output only. Resource name of the API Config. Format:
            projects/{project}/locations/global/apis/{api}/configs/{api_config}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Created time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Updated time.
        labels (Sequence[google.cloud.apigateway_v1.types.ApiConfig.LabelsEntry]):
            Optional. Resource labels to represent user-
            rovided metadata. Refer to cloud documentation
            on labels for more details.
            https://cloud.google.com/compute/docs/labeling-
            resources
        display_name (str):
            Optional. Display name.
        gateway_service_account (str):
            Immutable. The Google Cloud IAM Service Account that
            Gateways serving this config should use to authenticate to
            other services. This may either be the Service Account's
            email (``{ACCOUNT_ID}@{PROJECT}.iam.gserviceaccount.com``)
            or its full resource name
            (``projects/{PROJECT}/accounts/{UNIQUE_ID}``). This is most
            often used when the service is a GCP resource such as a
            Cloud Run Service or an IAP-secured service.
        service_config_id (str):
            Output only. The ID of the associated Service
            Config ( https://cloud.google.com/service-
            infrastructure/docs/glossary#config).
        state (google.cloud.apigateway_v1.types.ApiConfig.State):
            Output only. State of the API Config.
        openapi_documents (Sequence[google.cloud.apigateway_v1.types.ApiConfig.OpenApiDocument]):
            Optional. OpenAPI specification documents. If specified,
            grpc_services and managed_service_configs must not be
            included.
        grpc_services (Sequence[google.cloud.apigateway_v1.types.ApiConfig.GrpcServiceDefinition]):
            Optional. gRPC service definition files. If specified,
            openapi_documents must not be included.
        managed_service_configs (Sequence[google.cloud.apigateway_v1.types.ApiConfig.File]):
            Optional. Service Configuration files. At least one must be
            included when using gRPC service definitions. See
            https://cloud.google.com/endpoints/docs/grpc/grpc-service-config#service_configuration_overview
            for the expected file contents.

            If multiple files are specified, the files are merged with
            the following rules:

            -  All singular scalar fields are merged using "last one
               wins" semantics in the order of the files uploaded.
            -  Repeated fields are concatenated.
            -  Singular embedded messages are merged using these rules
               for nested fields.
    """

    class State(proto.Enum):
        r"""All the possible API Config states."""
        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        FAILED = 3
        DELETING = 4
        UPDATING = 5
        ACTIVATING = 6

    class File(proto.Message):
        r"""A lightweight description of a file.
        Attributes:
            path (str):
                The file path (full or relative path). This
                is typically the path of the file when it is
                uploaded.
            contents (bytes):
                The bytes that constitute the file.
        """

        path = proto.Field(proto.STRING, number=1,)
        contents = proto.Field(proto.BYTES, number=2,)

    class OpenApiDocument(proto.Message):
        r"""An OpenAPI Specification Document describing an API.
        Attributes:
            document (google.cloud.apigateway_v1.types.ApiConfig.File):
                The OpenAPI Specification document file.
        """

        document = proto.Field(proto.MESSAGE, number=1, message="ApiConfig.File",)

    class GrpcServiceDefinition(proto.Message):
        r"""A gRPC service definition.
        Attributes:
            file_descriptor_set (google.cloud.apigateway_v1.types.ApiConfig.File):
                Input only. File descriptor set, generated by protoc.

                To generate, use protoc with imports and source info
                included. For an example test.proto file, the following
                command would put the value in a new file named out.pb.

                $ protoc --include_imports --include_source_info test.proto
                -o out.pb
            source (Sequence[google.cloud.apigateway_v1.types.ApiConfig.File]):
                Optional. Uncompiled proto files associated with the
                descriptor set, used for display purposes (server-side
                compilation is not supported). These should match the inputs
                to 'protoc' command used to generate file_descriptor_set.
        """

        file_descriptor_set = proto.Field(
            proto.MESSAGE, number=1, message="ApiConfig.File",
        )
        source = proto.RepeatedField(proto.MESSAGE, number=2, message="ApiConfig.File",)

    name = proto.Field(proto.STRING, number=1,)
    create_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    labels = proto.MapField(proto.STRING, proto.STRING, number=4,)
    display_name = proto.Field(proto.STRING, number=5,)
    gateway_service_account = proto.Field(proto.STRING, number=14,)
    service_config_id = proto.Field(proto.STRING, number=12,)
    state = proto.Field(proto.ENUM, number=8, enum=State,)
    openapi_documents = proto.RepeatedField(
        proto.MESSAGE, number=9, message=OpenApiDocument,
    )
    grpc_services = proto.RepeatedField(
        proto.MESSAGE, number=10, message=GrpcServiceDefinition,
    )
    managed_service_configs = proto.RepeatedField(
        proto.MESSAGE, number=11, message=File,
    )


class Gateway(proto.Message):
    r"""A Gateway is an API-aware HTTP proxy. It performs API-Method
    and/or API-Consumer specific actions based on an API Config such
    as authentication, policy enforcement, and backend selection.

    Attributes:
        name (str):
            Output only. Resource name of the Gateway.
            Format:
            projects/{project}/locations/{location}/gateways/{gateway}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Created time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Updated time.
        labels (Sequence[google.cloud.apigateway_v1.types.Gateway.LabelsEntry]):
            Optional. Resource labels to represent user-
            rovided metadata. Refer to cloud documentation
            on labels for more details.
            https://cloud.google.com/compute/docs/labeling-
            resources
        display_name (str):
            Optional. Display name.
        api_config (str):
            Required. Resource name of the API Config for
            this Gateway. Format:
            projects/{project}/locations/global/apis/{api}/configs/{apiConfig}
        state (google.cloud.apigateway_v1.types.Gateway.State):
            Output only. The current state of the
            Gateway.
        default_hostname (str):
            Output only. The default API Gateway host name of the form
            ``{gateway_id}-{hash}.{region_code}.gateway.dev``.
    """

    class State(proto.Enum):
        r"""All the possible Gateway states."""
        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        FAILED = 3
        DELETING = 4
        UPDATING = 5

    name = proto.Field(proto.STRING, number=1,)
    create_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=3, message=timestamp_pb2.Timestamp,)
    labels = proto.MapField(proto.STRING, proto.STRING, number=4,)
    display_name = proto.Field(proto.STRING, number=5,)
    api_config = proto.Field(proto.STRING, number=6,)
    state = proto.Field(proto.ENUM, number=7, enum=State,)
    default_hostname = proto.Field(proto.STRING, number=9,)


class ListGatewaysRequest(proto.Message):
    r"""Request message for ApiGatewayService.ListGateways
    Attributes:
        parent (str):
            Required. Parent resource of the Gateway, of the form:
            ``projects/*/locations/*``
        page_size (int):
            Page size.
        page_token (str):
            Page token.
        filter (str):
            Filter.
        order_by (str):
            Order by parameters.
    """

    parent = proto.Field(proto.STRING, number=1,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)
    filter = proto.Field(proto.STRING, number=4,)
    order_by = proto.Field(proto.STRING, number=5,)


class ListGatewaysResponse(proto.Message):
    r"""Response message for ApiGatewayService.ListGateways
    Attributes:
        gateways (Sequence[google.cloud.apigateway_v1.types.Gateway]):
            Gateways.
        next_page_token (str):
            Next page token.
        unreachable_locations (Sequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    gateways = proto.RepeatedField(proto.MESSAGE, number=1, message="Gateway",)
    next_page_token = proto.Field(proto.STRING, number=2,)
    unreachable_locations = proto.RepeatedField(proto.STRING, number=3,)


class GetGatewayRequest(proto.Message):
    r"""Request message for ApiGatewayService.GetGateway
    Attributes:
        name (str):
            Required. Resource name of the form:
            ``projects/*/locations/*/gateways/*``
    """

    name = proto.Field(proto.STRING, number=1,)


class CreateGatewayRequest(proto.Message):
    r"""Request message for ApiGatewayService.CreateGateway
    Attributes:
        parent (str):
            Required. Parent resource of the Gateway, of the form:
            ``projects/*/locations/*``
        gateway_id (str):
            Required. Identifier to assign to the
            Gateway. Must be unique within scope of the
            parent resource.
        gateway (google.cloud.apigateway_v1.types.Gateway):
            Required. Gateway resource.
    """

    parent = proto.Field(proto.STRING, number=1,)
    gateway_id = proto.Field(proto.STRING, number=2,)
    gateway = proto.Field(proto.MESSAGE, number=3, message="Gateway",)


class UpdateGatewayRequest(proto.Message):
    r"""Request message for ApiGatewayService.UpdateGateway
    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the Gateway resource by the update. The fields specified
            in the update_mask are relative to the resource, not the
            full request. A field will be overwritten if it is in the
            mask. If the user does not provide a mask then all fields
            will be overwritten.
        gateway (google.cloud.apigateway_v1.types.Gateway):
            Required. Gateway resource.
    """

    update_mask = proto.Field(
        proto.MESSAGE, number=1, message=field_mask_pb2.FieldMask,
    )
    gateway = proto.Field(proto.MESSAGE, number=2, message="Gateway",)


class DeleteGatewayRequest(proto.Message):
    r"""Request message for ApiGatewayService.DeleteGateway
    Attributes:
        name (str):
            Required. Resource name of the form:
            ``projects/*/locations/*/gateways/*``
    """

    name = proto.Field(proto.STRING, number=1,)


class ListApisRequest(proto.Message):
    r"""Request message for ApiGatewayService.ListApis
    Attributes:
        parent (str):
            Required. Parent resource of the API, of the form:
            ``projects/*/locations/global``
        page_size (int):
            Page size.
        page_token (str):
            Page token.
        filter (str):
            Filter.
        order_by (str):
            Order by parameters.
    """

    parent = proto.Field(proto.STRING, number=1,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)
    filter = proto.Field(proto.STRING, number=4,)
    order_by = proto.Field(proto.STRING, number=5,)


class ListApisResponse(proto.Message):
    r"""Response message for ApiGatewayService.ListApis
    Attributes:
        apis (Sequence[google.cloud.apigateway_v1.types.Api]):
            APIs.
        next_page_token (str):
            Next page token.
        unreachable_locations (Sequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    apis = proto.RepeatedField(proto.MESSAGE, number=1, message="Api",)
    next_page_token = proto.Field(proto.STRING, number=2,)
    unreachable_locations = proto.RepeatedField(proto.STRING, number=3,)


class GetApiRequest(proto.Message):
    r"""Request message for ApiGatewayService.GetApi
    Attributes:
        name (str):
            Required. Resource name of the form:
            ``projects/*/locations/global/apis/*``
    """

    name = proto.Field(proto.STRING, number=1,)


class CreateApiRequest(proto.Message):
    r"""Request message for ApiGatewayService.CreateApi
    Attributes:
        parent (str):
            Required. Parent resource of the API, of the form:
            ``projects/*/locations/global``
        api_id (str):
            Required. Identifier to assign to the API.
            Must be unique within scope of the parent
            resource.
        api (google.cloud.apigateway_v1.types.Api):
            Required. API resource.
    """

    parent = proto.Field(proto.STRING, number=1,)
    api_id = proto.Field(proto.STRING, number=2,)
    api = proto.Field(proto.MESSAGE, number=3, message="Api",)


class UpdateApiRequest(proto.Message):
    r"""Request message for ApiGatewayService.UpdateApi
    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the Api resource by the update. The fields specified in
            the update_mask are relative to the resource, not the full
            request. A field will be overwritten if it is in the mask.
            If the user does not provide a mask then all fields will be
            overwritten.
        api (google.cloud.apigateway_v1.types.Api):
            Required. API resource.
    """

    update_mask = proto.Field(
        proto.MESSAGE, number=1, message=field_mask_pb2.FieldMask,
    )
    api = proto.Field(proto.MESSAGE, number=2, message="Api",)


class DeleteApiRequest(proto.Message):
    r"""Request message for ApiGatewayService.DeleteApi
    Attributes:
        name (str):
            Required. Resource name of the form:
            ``projects/*/locations/global/apis/*``
    """

    name = proto.Field(proto.STRING, number=1,)


class ListApiConfigsRequest(proto.Message):
    r"""Request message for ApiGatewayService.ListApiConfigs
    Attributes:
        parent (str):
            Required. Parent resource of the API Config, of the form:
            ``projects/*/locations/global/apis/*``
        page_size (int):
            Page size.
        page_token (str):
            Page token.
        filter (str):
            Filter.
        order_by (str):
            Order by parameters.
    """

    parent = proto.Field(proto.STRING, number=1,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)
    filter = proto.Field(proto.STRING, number=4,)
    order_by = proto.Field(proto.STRING, number=5,)


class ListApiConfigsResponse(proto.Message):
    r"""Response message for ApiGatewayService.ListApiConfigs
    Attributes:
        api_configs (Sequence[google.cloud.apigateway_v1.types.ApiConfig]):
            API Configs.
        next_page_token (str):
            Next page token.
        unreachable_locations (Sequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    api_configs = proto.RepeatedField(proto.MESSAGE, number=1, message="ApiConfig",)
    next_page_token = proto.Field(proto.STRING, number=2,)
    unreachable_locations = proto.RepeatedField(proto.STRING, number=3,)


class GetApiConfigRequest(proto.Message):
    r"""Request message for ApiGatewayService.GetApiConfig
    Attributes:
        name (str):
            Required. Resource name of the form:
            ``projects/*/locations/global/apis/*/configs/*``
        view (google.cloud.apigateway_v1.types.GetApiConfigRequest.ConfigView):
            Specifies which fields of the API Config are returned in the
            response. Defaults to ``BASIC`` view.
    """

    class ConfigView(proto.Enum):
        r"""Enum to control which fields should be included in the
        response.
        """
        CONFIG_VIEW_UNSPECIFIED = 0
        BASIC = 1
        FULL = 2

    name = proto.Field(proto.STRING, number=1,)
    view = proto.Field(proto.ENUM, number=3, enum=ConfigView,)


class CreateApiConfigRequest(proto.Message):
    r"""Request message for ApiGatewayService.CreateApiConfig
    Attributes:
        parent (str):
            Required. Parent resource of the API Config, of the form:
            ``projects/*/locations/global/apis/*``
        api_config_id (str):
            Required. Identifier to assign to the API
            Config. Must be unique within scope of the
            parent resource.
        api_config (google.cloud.apigateway_v1.types.ApiConfig):
            Required. API resource.
    """

    parent = proto.Field(proto.STRING, number=1,)
    api_config_id = proto.Field(proto.STRING, number=2,)
    api_config = proto.Field(proto.MESSAGE, number=3, message="ApiConfig",)


class UpdateApiConfigRequest(proto.Message):
    r"""Request message for ApiGatewayService.UpdateApiConfig
    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Field mask is used to specify the fields to be overwritten
            in the ApiConfig resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        api_config (google.cloud.apigateway_v1.types.ApiConfig):
            Required. API Config resource.
    """

    update_mask = proto.Field(
        proto.MESSAGE, number=1, message=field_mask_pb2.FieldMask,
    )
    api_config = proto.Field(proto.MESSAGE, number=2, message="ApiConfig",)


class DeleteApiConfigRequest(proto.Message):
    r"""Request message for ApiGatewayService.DeleteApiConfig
    Attributes:
        name (str):
            Required. Resource name of the form:
            ``projects/*/locations/global/apis/*/configs/*``
    """

    name = proto.Field(proto.STRING, number=1,)


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.
    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have [Operation.error][] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
        diagnostics (Sequence[google.cloud.apigateway_v1.types.OperationMetadata.Diagnostic]):
            Output only. Diagnostics generated during
            processing of configuration source files.
    """

    class Diagnostic(proto.Message):
        r"""Diagnostic information from configuration processing.
        Attributes:
            location (str):
                Location of the diagnostic.
            message (str):
                The diagnostic message.
        """

        location = proto.Field(proto.STRING, number=1,)
        message = proto.Field(proto.STRING, number=2,)

    create_time = proto.Field(proto.MESSAGE, number=1, message=timestamp_pb2.Timestamp,)
    end_time = proto.Field(proto.MESSAGE, number=2, message=timestamp_pb2.Timestamp,)
    target = proto.Field(proto.STRING, number=3,)
    verb = proto.Field(proto.STRING, number=4,)
    status_message = proto.Field(proto.STRING, number=5,)
    requested_cancellation = proto.Field(proto.BOOL, number=6,)
    api_version = proto.Field(proto.STRING, number=7,)
    diagnostics = proto.RepeatedField(proto.MESSAGE, number=8, message=Diagnostic,)


__all__ = tuple(sorted(__protobuf__.manifest))
