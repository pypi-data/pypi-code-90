# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/ndarray.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from metta.types import dtype_pb2 as proto_dot_dtype__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/ndarray.proto",
    package="",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x13proto/ndarray.proto\x1a\x11proto/dtype.proto"P\n\x07NDArray\x12\r\n\x05shape\x18\x01 \x03(\x03\x12\x15\n\x05\x64type\x18\x65 \x01(\x0b\x32\x06.dtype\x12\r\n\x04\x64\x61ta\x18\xc9\x01 \x01(\x0c\x12\x10\n\x07strides\x18\xad\x02 \x03(\x03\x62\x06proto3',
    dependencies=[
        proto_dot_dtype__pb2.DESCRIPTOR,
    ],
)


_NDARRAY = _descriptor.Descriptor(
    name="NDArray",
    full_name="NDArray",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="shape",
            full_name="NDArray.shape",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
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
            name="dtype",
            full_name="NDArray.dtype",
            index=1,
            number=101,
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
            name="data",
            full_name="NDArray.data",
            index=2,
            number=201,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
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
            name="strides",
            full_name="NDArray.strides",
            index=3,
            number=301,
            type=3,
            cpp_type=2,
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
    serialized_start=42,
    serialized_end=122,
)

_NDARRAY.fields_by_name["dtype"].message_type = proto_dot_dtype__pb2._DTYPE
DESCRIPTOR.message_types_by_name["NDArray"] = _NDARRAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NDArray = _reflection.GeneratedProtocolMessageType(
    "NDArray",
    (_message.Message,),
    {
        "DESCRIPTOR": _NDARRAY,
        "__module__": "metta.types.ndarray_pb2"
        # @@protoc_insertion_point(class_scope:NDArray)
    },
)
_sym_db.RegisterMessage(NDArray)


# @@protoc_insertion_point(module_scope)
