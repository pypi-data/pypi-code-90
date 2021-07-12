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
import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.api_core import gapic_v1  # type: ignore
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.automl_v1beta1.types import annotation_spec
from google.cloud.automl_v1beta1.types import column_spec
from google.cloud.automl_v1beta1.types import column_spec as gca_column_spec
from google.cloud.automl_v1beta1.types import dataset
from google.cloud.automl_v1beta1.types import dataset as gca_dataset
from google.cloud.automl_v1beta1.types import model
from google.cloud.automl_v1beta1.types import model_evaluation
from google.cloud.automl_v1beta1.types import service
from google.cloud.automl_v1beta1.types import table_spec
from google.cloud.automl_v1beta1.types import table_spec as gca_table_spec
from google.longrunning import operations_pb2  # type: ignore
from .base import AutoMlTransport, DEFAULT_CLIENT_INFO


class AutoMlGrpcTransport(AutoMlTransport):
    """gRPC backend transport for AutoMl.

    AutoML Server API.

    The resource names are assigned by the server. The server never
    reuses names that it has created after the resources with those
    names are deleted.

    An ID of a resource is the last element of the item's resource name.
    For
    ``projects/{project_id}/locations/{location_id}/datasets/{dataset_id}``,
    then the id for the item is ``{dataset_id}``.

    Currently the only supported ``location_id`` is "us-central1".

    On any input that is documented to expect a string parameter in
    snake_case or kebab-case, either of those cases is accepted.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "automl.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(
        cls,
        host: str = "automl.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service.
        """
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(self.grpc_channel)

        # Return the client from cache.
        return self._operations_client

    @property
    def create_dataset(
        self,
    ) -> Callable[[service.CreateDatasetRequest], gca_dataset.Dataset]:
        r"""Return a callable for the create dataset method over gRPC.

        Creates a dataset.

        Returns:
            Callable[[~.CreateDatasetRequest],
                    ~.Dataset]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_dataset" not in self._stubs:
            self._stubs["create_dataset"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/CreateDataset",
                request_serializer=service.CreateDatasetRequest.serialize,
                response_deserializer=gca_dataset.Dataset.deserialize,
            )
        return self._stubs["create_dataset"]

    @property
    def get_dataset(self) -> Callable[[service.GetDatasetRequest], dataset.Dataset]:
        r"""Return a callable for the get dataset method over gRPC.

        Gets a dataset.

        Returns:
            Callable[[~.GetDatasetRequest],
                    ~.Dataset]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_dataset" not in self._stubs:
            self._stubs["get_dataset"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/GetDataset",
                request_serializer=service.GetDatasetRequest.serialize,
                response_deserializer=dataset.Dataset.deserialize,
            )
        return self._stubs["get_dataset"]

    @property
    def list_datasets(
        self,
    ) -> Callable[[service.ListDatasetsRequest], service.ListDatasetsResponse]:
        r"""Return a callable for the list datasets method over gRPC.

        Lists datasets in a project.

        Returns:
            Callable[[~.ListDatasetsRequest],
                    ~.ListDatasetsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_datasets" not in self._stubs:
            self._stubs["list_datasets"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/ListDatasets",
                request_serializer=service.ListDatasetsRequest.serialize,
                response_deserializer=service.ListDatasetsResponse.deserialize,
            )
        return self._stubs["list_datasets"]

    @property
    def update_dataset(
        self,
    ) -> Callable[[service.UpdateDatasetRequest], gca_dataset.Dataset]:
        r"""Return a callable for the update dataset method over gRPC.

        Updates a dataset.

        Returns:
            Callable[[~.UpdateDatasetRequest],
                    ~.Dataset]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_dataset" not in self._stubs:
            self._stubs["update_dataset"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/UpdateDataset",
                request_serializer=service.UpdateDatasetRequest.serialize,
                response_deserializer=gca_dataset.Dataset.deserialize,
            )
        return self._stubs["update_dataset"]

    @property
    def delete_dataset(
        self,
    ) -> Callable[[service.DeleteDatasetRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete dataset method over gRPC.

        Deletes a dataset and all of its contents. Returns empty
        response in the
        [response][google.longrunning.Operation.response] field when it
        completes, and ``delete_details`` in the
        [metadata][google.longrunning.Operation.metadata] field.

        Returns:
            Callable[[~.DeleteDatasetRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_dataset" not in self._stubs:
            self._stubs["delete_dataset"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/DeleteDataset",
                request_serializer=service.DeleteDatasetRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_dataset"]

    @property
    def import_data(
        self,
    ) -> Callable[[service.ImportDataRequest], operations_pb2.Operation]:
        r"""Return a callable for the import data method over gRPC.

        Imports data into a dataset. For Tables this method can only be
        called on an empty Dataset.

        For Tables:

        -  A
           [schema_inference_version][google.cloud.automl.v1beta1.InputConfig.params]
           parameter must be explicitly set. Returns an empty response
           in the [response][google.longrunning.Operation.response]
           field when it completes.

        Returns:
            Callable[[~.ImportDataRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "import_data" not in self._stubs:
            self._stubs["import_data"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/ImportData",
                request_serializer=service.ImportDataRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["import_data"]

    @property
    def export_data(
        self,
    ) -> Callable[[service.ExportDataRequest], operations_pb2.Operation]:
        r"""Return a callable for the export data method over gRPC.

        Exports dataset's data to the provided output location. Returns
        an empty response in the
        [response][google.longrunning.Operation.response] field when it
        completes.

        Returns:
            Callable[[~.ExportDataRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_data" not in self._stubs:
            self._stubs["export_data"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/ExportData",
                request_serializer=service.ExportDataRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_data"]

    @property
    def get_annotation_spec(
        self,
    ) -> Callable[[service.GetAnnotationSpecRequest], annotation_spec.AnnotationSpec]:
        r"""Return a callable for the get annotation spec method over gRPC.

        Gets an annotation spec.

        Returns:
            Callable[[~.GetAnnotationSpecRequest],
                    ~.AnnotationSpec]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_annotation_spec" not in self._stubs:
            self._stubs["get_annotation_spec"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/GetAnnotationSpec",
                request_serializer=service.GetAnnotationSpecRequest.serialize,
                response_deserializer=annotation_spec.AnnotationSpec.deserialize,
            )
        return self._stubs["get_annotation_spec"]

    @property
    def get_table_spec(
        self,
    ) -> Callable[[service.GetTableSpecRequest], table_spec.TableSpec]:
        r"""Return a callable for the get table spec method over gRPC.

        Gets a table spec.

        Returns:
            Callable[[~.GetTableSpecRequest],
                    ~.TableSpec]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_table_spec" not in self._stubs:
            self._stubs["get_table_spec"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/GetTableSpec",
                request_serializer=service.GetTableSpecRequest.serialize,
                response_deserializer=table_spec.TableSpec.deserialize,
            )
        return self._stubs["get_table_spec"]

    @property
    def list_table_specs(
        self,
    ) -> Callable[[service.ListTableSpecsRequest], service.ListTableSpecsResponse]:
        r"""Return a callable for the list table specs method over gRPC.

        Lists table specs in a dataset.

        Returns:
            Callable[[~.ListTableSpecsRequest],
                    ~.ListTableSpecsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_table_specs" not in self._stubs:
            self._stubs["list_table_specs"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/ListTableSpecs",
                request_serializer=service.ListTableSpecsRequest.serialize,
                response_deserializer=service.ListTableSpecsResponse.deserialize,
            )
        return self._stubs["list_table_specs"]

    @property
    def update_table_spec(
        self,
    ) -> Callable[[service.UpdateTableSpecRequest], gca_table_spec.TableSpec]:
        r"""Return a callable for the update table spec method over gRPC.

        Updates a table spec.

        Returns:
            Callable[[~.UpdateTableSpecRequest],
                    ~.TableSpec]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_table_spec" not in self._stubs:
            self._stubs["update_table_spec"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/UpdateTableSpec",
                request_serializer=service.UpdateTableSpecRequest.serialize,
                response_deserializer=gca_table_spec.TableSpec.deserialize,
            )
        return self._stubs["update_table_spec"]

    @property
    def get_column_spec(
        self,
    ) -> Callable[[service.GetColumnSpecRequest], column_spec.ColumnSpec]:
        r"""Return a callable for the get column spec method over gRPC.

        Gets a column spec.

        Returns:
            Callable[[~.GetColumnSpecRequest],
                    ~.ColumnSpec]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_column_spec" not in self._stubs:
            self._stubs["get_column_spec"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/GetColumnSpec",
                request_serializer=service.GetColumnSpecRequest.serialize,
                response_deserializer=column_spec.ColumnSpec.deserialize,
            )
        return self._stubs["get_column_spec"]

    @property
    def list_column_specs(
        self,
    ) -> Callable[[service.ListColumnSpecsRequest], service.ListColumnSpecsResponse]:
        r"""Return a callable for the list column specs method over gRPC.

        Lists column specs in a table spec.

        Returns:
            Callable[[~.ListColumnSpecsRequest],
                    ~.ListColumnSpecsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_column_specs" not in self._stubs:
            self._stubs["list_column_specs"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/ListColumnSpecs",
                request_serializer=service.ListColumnSpecsRequest.serialize,
                response_deserializer=service.ListColumnSpecsResponse.deserialize,
            )
        return self._stubs["list_column_specs"]

    @property
    def update_column_spec(
        self,
    ) -> Callable[[service.UpdateColumnSpecRequest], gca_column_spec.ColumnSpec]:
        r"""Return a callable for the update column spec method over gRPC.

        Updates a column spec.

        Returns:
            Callable[[~.UpdateColumnSpecRequest],
                    ~.ColumnSpec]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_column_spec" not in self._stubs:
            self._stubs["update_column_spec"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/UpdateColumnSpec",
                request_serializer=service.UpdateColumnSpecRequest.serialize,
                response_deserializer=gca_column_spec.ColumnSpec.deserialize,
            )
        return self._stubs["update_column_spec"]

    @property
    def create_model(
        self,
    ) -> Callable[[service.CreateModelRequest], operations_pb2.Operation]:
        r"""Return a callable for the create model method over gRPC.

        Creates a model. Returns a Model in the
        [response][google.longrunning.Operation.response] field when it
        completes. When you create a model, several model evaluations
        are created for it: a global evaluation, and one evaluation for
        each annotation spec.

        Returns:
            Callable[[~.CreateModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_model" not in self._stubs:
            self._stubs["create_model"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/CreateModel",
                request_serializer=service.CreateModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_model"]

    @property
    def get_model(self) -> Callable[[service.GetModelRequest], model.Model]:
        r"""Return a callable for the get model method over gRPC.

        Gets a model.

        Returns:
            Callable[[~.GetModelRequest],
                    ~.Model]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_model" not in self._stubs:
            self._stubs["get_model"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/GetModel",
                request_serializer=service.GetModelRequest.serialize,
                response_deserializer=model.Model.deserialize,
            )
        return self._stubs["get_model"]

    @property
    def list_models(
        self,
    ) -> Callable[[service.ListModelsRequest], service.ListModelsResponse]:
        r"""Return a callable for the list models method over gRPC.

        Lists models.

        Returns:
            Callable[[~.ListModelsRequest],
                    ~.ListModelsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_models" not in self._stubs:
            self._stubs["list_models"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/ListModels",
                request_serializer=service.ListModelsRequest.serialize,
                response_deserializer=service.ListModelsResponse.deserialize,
            )
        return self._stubs["list_models"]

    @property
    def delete_model(
        self,
    ) -> Callable[[service.DeleteModelRequest], operations_pb2.Operation]:
        r"""Return a callable for the delete model method over gRPC.

        Deletes a model. Returns ``google.protobuf.Empty`` in the
        [response][google.longrunning.Operation.response] field when it
        completes, and ``delete_details`` in the
        [metadata][google.longrunning.Operation.metadata] field.

        Returns:
            Callable[[~.DeleteModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_model" not in self._stubs:
            self._stubs["delete_model"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/DeleteModel",
                request_serializer=service.DeleteModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_model"]

    @property
    def deploy_model(
        self,
    ) -> Callable[[service.DeployModelRequest], operations_pb2.Operation]:
        r"""Return a callable for the deploy model method over gRPC.

        Deploys a model. If a model is already deployed, deploying it
        with the same parameters has no effect. Deploying with different
        parametrs (as e.g. changing

        [node_number][google.cloud.automl.v1beta1.ImageObjectDetectionModelDeploymentMetadata.node_number])
        will reset the deployment state without pausing the model's
        availability.

        Only applicable for Text Classification, Image Object Detection
        , Tables, and Image Segmentation; all other domains manage
        deployment automatically.

        Returns an empty response in the
        [response][google.longrunning.Operation.response] field when it
        completes.

        Returns:
            Callable[[~.DeployModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "deploy_model" not in self._stubs:
            self._stubs["deploy_model"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/DeployModel",
                request_serializer=service.DeployModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["deploy_model"]

    @property
    def undeploy_model(
        self,
    ) -> Callable[[service.UndeployModelRequest], operations_pb2.Operation]:
        r"""Return a callable for the undeploy model method over gRPC.

        Undeploys a model. If the model is not deployed this method has
        no effect.

        Only applicable for Text Classification, Image Object Detection
        and Tables; all other domains manage deployment automatically.

        Returns an empty response in the
        [response][google.longrunning.Operation.response] field when it
        completes.

        Returns:
            Callable[[~.UndeployModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undeploy_model" not in self._stubs:
            self._stubs["undeploy_model"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/UndeployModel",
                request_serializer=service.UndeployModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["undeploy_model"]

    @property
    def export_model(
        self,
    ) -> Callable[[service.ExportModelRequest], operations_pb2.Operation]:
        r"""Return a callable for the export model method over gRPC.

        Exports a trained, "export-able", model to a user specified
        Google Cloud Storage location. A model is considered export-able
        if and only if it has an export format defined for it in

        [ModelExportOutputConfig][google.cloud.automl.v1beta1.ModelExportOutputConfig].

        Returns an empty response in the
        [response][google.longrunning.Operation.response] field when it
        completes.

        Returns:
            Callable[[~.ExportModelRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_model" not in self._stubs:
            self._stubs["export_model"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/ExportModel",
                request_serializer=service.ExportModelRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_model"]

    @property
    def export_evaluated_examples(
        self,
    ) -> Callable[[service.ExportEvaluatedExamplesRequest], operations_pb2.Operation]:
        r"""Return a callable for the export evaluated examples method over gRPC.

        Exports examples on which the model was evaluated (i.e. which
        were in the TEST set of the dataset the model was created from),
        together with their ground truth annotations and the annotations
        created (predicted) by the model. The examples, ground truth and
        predictions are exported in the state they were at the moment
        the model was evaluated.

        This export is available only for 30 days since the model
        evaluation is created.

        Currently only available for Tables.

        Returns an empty response in the
        [response][google.longrunning.Operation.response] field when it
        completes.

        Returns:
            Callable[[~.ExportEvaluatedExamplesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "export_evaluated_examples" not in self._stubs:
            self._stubs["export_evaluated_examples"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/ExportEvaluatedExamples",
                request_serializer=service.ExportEvaluatedExamplesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["export_evaluated_examples"]

    @property
    def get_model_evaluation(
        self,
    ) -> Callable[
        [service.GetModelEvaluationRequest], model_evaluation.ModelEvaluation
    ]:
        r"""Return a callable for the get model evaluation method over gRPC.

        Gets a model evaluation.

        Returns:
            Callable[[~.GetModelEvaluationRequest],
                    ~.ModelEvaluation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_model_evaluation" not in self._stubs:
            self._stubs["get_model_evaluation"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/GetModelEvaluation",
                request_serializer=service.GetModelEvaluationRequest.serialize,
                response_deserializer=model_evaluation.ModelEvaluation.deserialize,
            )
        return self._stubs["get_model_evaluation"]

    @property
    def list_model_evaluations(
        self,
    ) -> Callable[
        [service.ListModelEvaluationsRequest], service.ListModelEvaluationsResponse
    ]:
        r"""Return a callable for the list model evaluations method over gRPC.

        Lists model evaluations.

        Returns:
            Callable[[~.ListModelEvaluationsRequest],
                    ~.ListModelEvaluationsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_model_evaluations" not in self._stubs:
            self._stubs["list_model_evaluations"] = self.grpc_channel.unary_unary(
                "/google.cloud.automl.v1beta1.AutoMl/ListModelEvaluations",
                request_serializer=service.ListModelEvaluationsRequest.serialize,
                response_deserializer=service.ListModelEvaluationsResponse.deserialize,
            )
        return self._stubs["list_model_evaluations"]


__all__ = ("AutoMlGrpcTransport",)
