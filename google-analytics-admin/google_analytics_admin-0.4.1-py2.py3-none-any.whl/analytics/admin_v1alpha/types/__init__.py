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
from .analytics_admin import (
    ArchiveCustomDimensionRequest,
    ArchiveCustomMetricRequest,
    AuditUserLinksRequest,
    AuditUserLinksResponse,
    BatchCreateUserLinksRequest,
    BatchCreateUserLinksResponse,
    BatchDeleteUserLinksRequest,
    BatchGetUserLinksRequest,
    BatchGetUserLinksResponse,
    BatchUpdateUserLinksRequest,
    BatchUpdateUserLinksResponse,
    CreateConversionEventRequest,
    CreateCustomDimensionRequest,
    CreateCustomMetricRequest,
    CreateFirebaseLinkRequest,
    CreateGoogleAdsLinkRequest,
    CreateMeasurementProtocolSecretRequest,
    CreatePropertyRequest,
    CreateUserLinkRequest,
    CreateWebDataStreamRequest,
    DeleteAccountRequest,
    DeleteAndroidAppDataStreamRequest,
    DeleteConversionEventRequest,
    DeleteFirebaseLinkRequest,
    DeleteGoogleAdsLinkRequest,
    DeleteIosAppDataStreamRequest,
    DeleteMeasurementProtocolSecretRequest,
    DeletePropertyRequest,
    DeleteUserLinkRequest,
    DeleteWebDataStreamRequest,
    GetAccountRequest,
    GetAndroidAppDataStreamRequest,
    GetConversionEventRequest,
    GetCustomDimensionRequest,
    GetCustomMetricRequest,
    GetDataSharingSettingsRequest,
    GetEnhancedMeasurementSettingsRequest,
    GetGlobalSiteTagRequest,
    GetGoogleSignalsSettingsRequest,
    GetIosAppDataStreamRequest,
    GetMeasurementProtocolSecretRequest,
    GetPropertyRequest,
    GetUserLinkRequest,
    GetWebDataStreamRequest,
    ListAccountsRequest,
    ListAccountsResponse,
    ListAccountSummariesRequest,
    ListAccountSummariesResponse,
    ListAndroidAppDataStreamsRequest,
    ListAndroidAppDataStreamsResponse,
    ListConversionEventsRequest,
    ListConversionEventsResponse,
    ListCustomDimensionsRequest,
    ListCustomDimensionsResponse,
    ListCustomMetricsRequest,
    ListCustomMetricsResponse,
    ListFirebaseLinksRequest,
    ListFirebaseLinksResponse,
    ListGoogleAdsLinksRequest,
    ListGoogleAdsLinksResponse,
    ListIosAppDataStreamsRequest,
    ListIosAppDataStreamsResponse,
    ListMeasurementProtocolSecretsRequest,
    ListMeasurementProtocolSecretsResponse,
    ListPropertiesRequest,
    ListPropertiesResponse,
    ListUserLinksRequest,
    ListUserLinksResponse,
    ListWebDataStreamsRequest,
    ListWebDataStreamsResponse,
    ProvisionAccountTicketRequest,
    ProvisionAccountTicketResponse,
    SearchChangeHistoryEventsRequest,
    SearchChangeHistoryEventsResponse,
    UpdateAccountRequest,
    UpdateAndroidAppDataStreamRequest,
    UpdateCustomDimensionRequest,
    UpdateCustomMetricRequest,
    UpdateEnhancedMeasurementSettingsRequest,
    UpdateFirebaseLinkRequest,
    UpdateGoogleAdsLinkRequest,
    UpdateGoogleSignalsSettingsRequest,
    UpdateIosAppDataStreamRequest,
    UpdateMeasurementProtocolSecretRequest,
    UpdatePropertyRequest,
    UpdateUserLinkRequest,
    UpdateWebDataStreamRequest,
)
from .resources import (
    Account,
    AccountSummary,
    AndroidAppDataStream,
    AuditUserLink,
    ChangeHistoryChange,
    ChangeHistoryEvent,
    ConversionEvent,
    CustomDimension,
    CustomMetric,
    DataSharingSettings,
    EnhancedMeasurementSettings,
    FirebaseLink,
    GlobalSiteTag,
    GoogleAdsLink,
    GoogleSignalsSettings,
    IosAppDataStream,
    MeasurementProtocolSecret,
    Property,
    PropertySummary,
    UserLink,
    WebDataStream,
    ActionType,
    ActorType,
    ChangeHistoryResourceType,
    GoogleSignalsConsent,
    GoogleSignalsState,
    IndustryCategory,
    MaximumUserAccess,
)

__all__ = (
    "ArchiveCustomDimensionRequest",
    "ArchiveCustomMetricRequest",
    "AuditUserLinksRequest",
    "AuditUserLinksResponse",
    "BatchCreateUserLinksRequest",
    "BatchCreateUserLinksResponse",
    "BatchDeleteUserLinksRequest",
    "BatchGetUserLinksRequest",
    "BatchGetUserLinksResponse",
    "BatchUpdateUserLinksRequest",
    "BatchUpdateUserLinksResponse",
    "CreateConversionEventRequest",
    "CreateCustomDimensionRequest",
    "CreateCustomMetricRequest",
    "CreateFirebaseLinkRequest",
    "CreateGoogleAdsLinkRequest",
    "CreateMeasurementProtocolSecretRequest",
    "CreatePropertyRequest",
    "CreateUserLinkRequest",
    "CreateWebDataStreamRequest",
    "DeleteAccountRequest",
    "DeleteAndroidAppDataStreamRequest",
    "DeleteConversionEventRequest",
    "DeleteFirebaseLinkRequest",
    "DeleteGoogleAdsLinkRequest",
    "DeleteIosAppDataStreamRequest",
    "DeleteMeasurementProtocolSecretRequest",
    "DeletePropertyRequest",
    "DeleteUserLinkRequest",
    "DeleteWebDataStreamRequest",
    "GetAccountRequest",
    "GetAndroidAppDataStreamRequest",
    "GetConversionEventRequest",
    "GetCustomDimensionRequest",
    "GetCustomMetricRequest",
    "GetDataSharingSettingsRequest",
    "GetEnhancedMeasurementSettingsRequest",
    "GetGlobalSiteTagRequest",
    "GetGoogleSignalsSettingsRequest",
    "GetIosAppDataStreamRequest",
    "GetMeasurementProtocolSecretRequest",
    "GetPropertyRequest",
    "GetUserLinkRequest",
    "GetWebDataStreamRequest",
    "ListAccountsRequest",
    "ListAccountsResponse",
    "ListAccountSummariesRequest",
    "ListAccountSummariesResponse",
    "ListAndroidAppDataStreamsRequest",
    "ListAndroidAppDataStreamsResponse",
    "ListConversionEventsRequest",
    "ListConversionEventsResponse",
    "ListCustomDimensionsRequest",
    "ListCustomDimensionsResponse",
    "ListCustomMetricsRequest",
    "ListCustomMetricsResponse",
    "ListFirebaseLinksRequest",
    "ListFirebaseLinksResponse",
    "ListGoogleAdsLinksRequest",
    "ListGoogleAdsLinksResponse",
    "ListIosAppDataStreamsRequest",
    "ListIosAppDataStreamsResponse",
    "ListMeasurementProtocolSecretsRequest",
    "ListMeasurementProtocolSecretsResponse",
    "ListPropertiesRequest",
    "ListPropertiesResponse",
    "ListUserLinksRequest",
    "ListUserLinksResponse",
    "ListWebDataStreamsRequest",
    "ListWebDataStreamsResponse",
    "ProvisionAccountTicketRequest",
    "ProvisionAccountTicketResponse",
    "SearchChangeHistoryEventsRequest",
    "SearchChangeHistoryEventsResponse",
    "UpdateAccountRequest",
    "UpdateAndroidAppDataStreamRequest",
    "UpdateCustomDimensionRequest",
    "UpdateCustomMetricRequest",
    "UpdateEnhancedMeasurementSettingsRequest",
    "UpdateFirebaseLinkRequest",
    "UpdateGoogleAdsLinkRequest",
    "UpdateGoogleSignalsSettingsRequest",
    "UpdateIosAppDataStreamRequest",
    "UpdateMeasurementProtocolSecretRequest",
    "UpdatePropertyRequest",
    "UpdateUserLinkRequest",
    "UpdateWebDataStreamRequest",
    "Account",
    "AccountSummary",
    "AndroidAppDataStream",
    "AuditUserLink",
    "ChangeHistoryChange",
    "ChangeHistoryEvent",
    "ConversionEvent",
    "CustomDimension",
    "CustomMetric",
    "DataSharingSettings",
    "EnhancedMeasurementSettings",
    "FirebaseLink",
    "GlobalSiteTag",
    "GoogleAdsLink",
    "GoogleSignalsSettings",
    "IosAppDataStream",
    "MeasurementProtocolSecret",
    "Property",
    "PropertySummary",
    "UserLink",
    "WebDataStream",
    "ActionType",
    "ActorType",
    "ChangeHistoryResourceType",
    "GoogleSignalsConsent",
    "GoogleSignalsState",
    "IndustryCategory",
    "MaximumUserAccess",
)
