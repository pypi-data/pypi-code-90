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

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/identity/accesscontextmanager/v1/service_perimeter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/identity/accesscontextmanager/v1/service_perimeter.proto",
    package="google.identity.accesscontextmanager.v1",
    syntax="proto3",
    serialized_options=b"\n+com.google.identity.accesscontextmanager.v1B\025ServicePerimeterProtoP\001Z[google.golang.org/genproto/googleapis/identity/accesscontextmanager/v1;accesscontextmanager\242\002\004GACM\252\002'Google.Identity.AccessContextManager.V1\312\002'Google\\Identity\\AccessContextManager\\V1\352\002*Google::Identity::AccessContextManager::V1",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n?google/identity/accesscontextmanager/v1/service_perimeter.proto\x12'google.identity.accesscontextmanager.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto\"\x92\x04\n\x10ServicePerimeter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12/\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12_\n\x0eperimeter_type\x18\x06 \x01(\x0e\x32G.google.identity.accesscontextmanager.v1.ServicePerimeter.PerimeterType\x12O\n\x06status\x18\x07 \x01(\x0b\x32?.google.identity.accesscontextmanager.v1.ServicePerimeterConfig\x12M\n\x04spec\x18\x08 \x01(\x0b\x32?.google.identity.accesscontextmanager.v1.ServicePerimeterConfig\x12!\n\x19use_explicit_dry_run_spec\x18\t \x01(\x08\"F\n\rPerimeterType\x12\x1a\n\x16PERIMETER_TYPE_REGULAR\x10\x00\x12\x19\n\x15PERIMETER_TYPE_BRIDGE\x10\x01\"\xa6\x02\n\x16ServicePerimeterConfig\x12\x11\n\tresources\x18\x01 \x03(\t\x12\x15\n\raccess_levels\x18\x02 \x03(\t\x12\x1b\n\x13restricted_services\x18\x04 \x03(\t\x12v\n\x17vpc_accessible_services\x18\n \x01(\x0b\x32U.google.identity.accesscontextmanager.v1.ServicePerimeterConfig.VpcAccessibleServices\x1aM\n\x15VpcAccessibleServices\x12\x1a\n\x12\x65nable_restriction\x18\x01 \x01(\x08\x12\x18\n\x10\x61llowed_services\x18\x02 \x03(\tB\xab\x02\n+com.google.identity.accesscontextmanager.v1B\x15ServicePerimeterProtoP\x01Z[google.golang.org/genproto/googleapis/identity/accesscontextmanager/v1;accesscontextmanager\xa2\x02\x04GACM\xaa\x02'Google.Identity.AccessContextManager.V1\xca\x02'Google\\Identity\\AccessContextManager\\V1\xea\x02*Google::Identity::AccessContextManager::V1b\x06proto3",
    dependencies=[
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_SERVICEPERIMETER_PERIMETERTYPE = _descriptor.EnumDescriptor(
    name="PerimeterType",
    full_name="google.identity.accesscontextmanager.v1.ServicePerimeter.PerimeterType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="PERIMETER_TYPE_REGULAR",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="PERIMETER_TYPE_BRIDGE",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=632,
    serialized_end=702,
)
_sym_db.RegisterEnumDescriptor(_SERVICEPERIMETER_PERIMETERTYPE)


_SERVICEPERIMETER = _descriptor.Descriptor(
    name="ServicePerimeter",
    full_name="google.identity.accesscontextmanager.v1.ServicePerimeter",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeter.name",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="title",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeter.title",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeter.description",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeter.create_time",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="update_time",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeter.update_time",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="perimeter_type",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeter.perimeter_type",
            index=5,
            number=6,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="status",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeter.status",
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="spec",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeter.spec",
            index=7,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="use_explicit_dry_run_spec",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeter.use_explicit_dry_run_spec",
            index=8,
            number=9,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_SERVICEPERIMETER_PERIMETERTYPE,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=172,
    serialized_end=702,
)


_SERVICEPERIMETERCONFIG_VPCACCESSIBLESERVICES = _descriptor.Descriptor(
    name="VpcAccessibleServices",
    full_name="google.identity.accesscontextmanager.v1.ServicePerimeterConfig.VpcAccessibleServices",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="enable_restriction",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeterConfig.VpcAccessibleServices.enable_restriction",
            index=0,
            number=1,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="allowed_services",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeterConfig.VpcAccessibleServices.allowed_services",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=922,
    serialized_end=999,
)

_SERVICEPERIMETERCONFIG = _descriptor.Descriptor(
    name="ServicePerimeterConfig",
    full_name="google.identity.accesscontextmanager.v1.ServicePerimeterConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="resources",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeterConfig.resources",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="access_levels",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeterConfig.access_levels",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="restricted_services",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeterConfig.restricted_services",
            index=2,
            number=4,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="vpc_accessible_services",
            full_name="google.identity.accesscontextmanager.v1.ServicePerimeterConfig.vpc_accessible_services",
            index=3,
            number=10,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[_SERVICEPERIMETERCONFIG_VPCACCESSIBLESERVICES,],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=705,
    serialized_end=999,
)

_SERVICEPERIMETER.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SERVICEPERIMETER.fields_by_name[
    "update_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SERVICEPERIMETER.fields_by_name[
    "perimeter_type"
].enum_type = _SERVICEPERIMETER_PERIMETERTYPE
_SERVICEPERIMETER.fields_by_name["status"].message_type = _SERVICEPERIMETERCONFIG
_SERVICEPERIMETER.fields_by_name["spec"].message_type = _SERVICEPERIMETERCONFIG
_SERVICEPERIMETER_PERIMETERTYPE.containing_type = _SERVICEPERIMETER
_SERVICEPERIMETERCONFIG_VPCACCESSIBLESERVICES.containing_type = _SERVICEPERIMETERCONFIG
_SERVICEPERIMETERCONFIG.fields_by_name[
    "vpc_accessible_services"
].message_type = _SERVICEPERIMETERCONFIG_VPCACCESSIBLESERVICES
DESCRIPTOR.message_types_by_name["ServicePerimeter"] = _SERVICEPERIMETER
DESCRIPTOR.message_types_by_name["ServicePerimeterConfig"] = _SERVICEPERIMETERCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServicePerimeter = _reflection.GeneratedProtocolMessageType(
    "ServicePerimeter",
    (_message.Message,),
    {
        "DESCRIPTOR": _SERVICEPERIMETER,
        "__module__": "google.identity.accesscontextmanager.v1.service_perimeter_pb2"
        # @@protoc_insertion_point(class_scope:google.identity.accesscontextmanager.v1.ServicePerimeter)
    },
)
_sym_db.RegisterMessage(ServicePerimeter)

ServicePerimeterConfig = _reflection.GeneratedProtocolMessageType(
    "ServicePerimeterConfig",
    (_message.Message,),
    {
        "VpcAccessibleServices": _reflection.GeneratedProtocolMessageType(
            "VpcAccessibleServices",
            (_message.Message,),
            {
                "DESCRIPTOR": _SERVICEPERIMETERCONFIG_VPCACCESSIBLESERVICES,
                "__module__": "google.identity.accesscontextmanager.v1.service_perimeter_pb2"
                # @@protoc_insertion_point(class_scope:google.identity.accesscontextmanager.v1.ServicePerimeterConfig.VpcAccessibleServices)
            },
        ),
        "DESCRIPTOR": _SERVICEPERIMETERCONFIG,
        "__module__": "google.identity.accesscontextmanager.v1.service_perimeter_pb2"
        # @@protoc_insertion_point(class_scope:google.identity.accesscontextmanager.v1.ServicePerimeterConfig)
    },
)
_sym_db.RegisterMessage(ServicePerimeterConfig)
_sym_db.RegisterMessage(ServicePerimeterConfig.VpcAccessibleServices)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
