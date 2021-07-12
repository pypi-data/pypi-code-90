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
from google.api_core import gapic_v1  # type: ignore
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.dialogflow_v2beta1.types import participant
from google.cloud.dialogflow_v2beta1.types import participant as gcd_participant
from .base import ParticipantsTransport, DEFAULT_CLIENT_INFO


class ParticipantsGrpcTransport(ParticipantsTransport):
    """gRPC backend transport for Participants.

    Service for managing
    [Participants][google.cloud.dialogflow.v2beta1.Participant].

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
        host: str = "dialogflow.googleapis.com",
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
        host: str = "dialogflow.googleapis.com",
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
    def create_participant(
        self,
    ) -> Callable[
        [gcd_participant.CreateParticipantRequest], gcd_participant.Participant
    ]:
        r"""Return a callable for the create participant method over gRPC.

        Creates a new participant in a conversation.

        Returns:
            Callable[[~.CreateParticipantRequest],
                    ~.Participant]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_participant" not in self._stubs:
            self._stubs["create_participant"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Participants/CreateParticipant",
                request_serializer=gcd_participant.CreateParticipantRequest.serialize,
                response_deserializer=gcd_participant.Participant.deserialize,
            )
        return self._stubs["create_participant"]

    @property
    def get_participant(
        self,
    ) -> Callable[[participant.GetParticipantRequest], participant.Participant]:
        r"""Return a callable for the get participant method over gRPC.

        Retrieves a conversation participant.

        Returns:
            Callable[[~.GetParticipantRequest],
                    ~.Participant]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_participant" not in self._stubs:
            self._stubs["get_participant"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Participants/GetParticipant",
                request_serializer=participant.GetParticipantRequest.serialize,
                response_deserializer=participant.Participant.deserialize,
            )
        return self._stubs["get_participant"]

    @property
    def list_participants(
        self,
    ) -> Callable[
        [participant.ListParticipantsRequest], participant.ListParticipantsResponse
    ]:
        r"""Return a callable for the list participants method over gRPC.

        Returns the list of all participants in the specified
        conversation.

        Returns:
            Callable[[~.ListParticipantsRequest],
                    ~.ListParticipantsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_participants" not in self._stubs:
            self._stubs["list_participants"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Participants/ListParticipants",
                request_serializer=participant.ListParticipantsRequest.serialize,
                response_deserializer=participant.ListParticipantsResponse.deserialize,
            )
        return self._stubs["list_participants"]

    @property
    def update_participant(
        self,
    ) -> Callable[
        [gcd_participant.UpdateParticipantRequest], gcd_participant.Participant
    ]:
        r"""Return a callable for the update participant method over gRPC.

        Updates the specified participant.

        Returns:
            Callable[[~.UpdateParticipantRequest],
                    ~.Participant]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_participant" not in self._stubs:
            self._stubs["update_participant"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Participants/UpdateParticipant",
                request_serializer=gcd_participant.UpdateParticipantRequest.serialize,
                response_deserializer=gcd_participant.Participant.deserialize,
            )
        return self._stubs["update_participant"]

    @property
    def analyze_content(
        self,
    ) -> Callable[
        [gcd_participant.AnalyzeContentRequest], gcd_participant.AnalyzeContentResponse
    ]:
        r"""Return a callable for the analyze content method over gRPC.

        Adds a text (chat, for example), or audio (phone recording, for
        example) message from a participant into the conversation.

        Note: Always use agent versions for production traffic sent to
        virtual agents. See `Versions and
        environments <https://cloud.google.com/dialogflow/es/docs/agents-versions>`__.

        Returns:
            Callable[[~.AnalyzeContentRequest],
                    ~.AnalyzeContentResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "analyze_content" not in self._stubs:
            self._stubs["analyze_content"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Participants/AnalyzeContent",
                request_serializer=gcd_participant.AnalyzeContentRequest.serialize,
                response_deserializer=gcd_participant.AnalyzeContentResponse.deserialize,
            )
        return self._stubs["analyze_content"]

    @property
    def suggest_articles(
        self,
    ) -> Callable[
        [participant.SuggestArticlesRequest], participant.SuggestArticlesResponse
    ]:
        r"""Return a callable for the suggest articles method over gRPC.

        Gets suggested articles for a participant based on specific
        historical messages.

        Note that
        [ListSuggestions][google.cloud.dialogflow.v2beta1.Participants.ListSuggestions]
        will only list the auto-generated suggestions, while
        [CompileSuggestion][google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion]
        will try to compile suggestion based on the provided
        conversation context in the real time.

        Returns:
            Callable[[~.SuggestArticlesRequest],
                    ~.SuggestArticlesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "suggest_articles" not in self._stubs:
            self._stubs["suggest_articles"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Participants/SuggestArticles",
                request_serializer=participant.SuggestArticlesRequest.serialize,
                response_deserializer=participant.SuggestArticlesResponse.deserialize,
            )
        return self._stubs["suggest_articles"]

    @property
    def suggest_faq_answers(
        self,
    ) -> Callable[
        [participant.SuggestFaqAnswersRequest], participant.SuggestFaqAnswersResponse
    ]:
        r"""Return a callable for the suggest faq answers method over gRPC.

        Gets suggested faq answers for a participant based on
        specific historical messages.

        Returns:
            Callable[[~.SuggestFaqAnswersRequest],
                    ~.SuggestFaqAnswersResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "suggest_faq_answers" not in self._stubs:
            self._stubs["suggest_faq_answers"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Participants/SuggestFaqAnswers",
                request_serializer=participant.SuggestFaqAnswersRequest.serialize,
                response_deserializer=participant.SuggestFaqAnswersResponse.deserialize,
            )
        return self._stubs["suggest_faq_answers"]

    @property
    def suggest_smart_replies(
        self,
    ) -> Callable[
        [participant.SuggestSmartRepliesRequest],
        participant.SuggestSmartRepliesResponse,
    ]:
        r"""Return a callable for the suggest smart replies method over gRPC.

        Gets smart replies for a participant based on
        specific historical messages.

        Returns:
            Callable[[~.SuggestSmartRepliesRequest],
                    ~.SuggestSmartRepliesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "suggest_smart_replies" not in self._stubs:
            self._stubs["suggest_smart_replies"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Participants/SuggestSmartReplies",
                request_serializer=participant.SuggestSmartRepliesRequest.serialize,
                response_deserializer=participant.SuggestSmartRepliesResponse.deserialize,
            )
        return self._stubs["suggest_smart_replies"]

    @property
    def list_suggestions(
        self,
    ) -> Callable[
        [participant.ListSuggestionsRequest], participant.ListSuggestionsResponse
    ]:
        r"""Return a callable for the list suggestions method over gRPC.

        Deprecated: Use inline suggestion, event based suggestion or
        Suggestion\* API instead. See
        [HumanAgentAssistantConfig.name][google.cloud.dialogflow.v2beta1.HumanAgentAssistantConfig.name]
        for more details. Removal Date: 2020-09-01.

        Retrieves suggestions for live agents.

        This method should be used by human agent client software to
        fetch auto generated suggestions in real-time, while the
        conversation with an end user is in progress. The functionality
        is implemented in terms of the `list
        pagination <https://cloud.google.com/apis/design/design_patterns#list_pagination>`__
        design pattern. The client app should use the
        ``next_page_token`` field to fetch the next batch of
        suggestions. ``suggestions`` are sorted by ``create_time`` in
        descending order. To fetch latest suggestion, just set
        ``page_size`` to 1. To fetch new suggestions without
        duplication, send request with filter
        ``create_time_epoch_microseconds > [first item's create_time of previous request]``
        and empty page_token.

        Returns:
            Callable[[~.ListSuggestionsRequest],
                    ~.ListSuggestionsResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_suggestions" not in self._stubs:
            self._stubs["list_suggestions"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Participants/ListSuggestions",
                request_serializer=participant.ListSuggestionsRequest.serialize,
                response_deserializer=participant.ListSuggestionsResponse.deserialize,
            )
        return self._stubs["list_suggestions"]

    @property
    def compile_suggestion(
        self,
    ) -> Callable[
        [participant.CompileSuggestionRequest], participant.CompileSuggestionResponse
    ]:
        r"""Return a callable for the compile suggestion method over gRPC.

        Deprecated. use
        [SuggestArticles][google.cloud.dialogflow.v2beta1.Participants.SuggestArticles]
        and
        [SuggestFaqAnswers][google.cloud.dialogflow.v2beta1.Participants.SuggestFaqAnswers]
        instead.

        Gets suggestions for a participant based on specific historical
        messages.

        Note that
        [ListSuggestions][google.cloud.dialogflow.v2beta1.Participants.ListSuggestions]
        will only list the auto-generated suggestions, while
        [CompileSuggestion][google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion]
        will try to compile suggestion based on the provided
        conversation context in the real time.

        Returns:
            Callable[[~.CompileSuggestionRequest],
                    ~.CompileSuggestionResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "compile_suggestion" not in self._stubs:
            self._stubs["compile_suggestion"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2beta1.Participants/CompileSuggestion",
                request_serializer=participant.CompileSuggestionRequest.serialize,
                response_deserializer=participant.CompileSuggestionResponse.deserialize,
            )
        return self._stubs["compile_suggestion"]


__all__ = ("ParticipantsGrpcTransport",)
