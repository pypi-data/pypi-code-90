# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cirq_google/api/v1/operations.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cirq_google/api/v1/operations.proto',
  package='cirq.google.api.v1',
  syntax='proto3',
  serialized_options=_b('\n\035com.google.cirq.google.api.v1B\017OperationsProtoP\001'),
  serialized_pb=_b('\n#cirq_google/api/v1/operations.proto\x12\x12\x63irq.google.api.v1\"!\n\x05Qubit\x12\x0b\n\x03row\x18\x01 \x01(\x05\x12\x0b\n\x03\x63ol\x18\x02 \x01(\x05\"E\n\x12ParameterizedFloat\x12\r\n\x03raw\x18\x01 \x01(\x02H\x00\x12\x17\n\rparameter_key\x18\x02 \x01(\tH\x00\x42\x07\n\x05value\"\xae\x01\n\x04\x45xpW\x12)\n\x06target\x18\x01 \x01(\x0b\x32\x19.cirq.google.api.v1.Qubit\x12?\n\x0f\x61xis_half_turns\x18\x02 \x01(\x0b\x32&.cirq.google.api.v1.ParameterizedFloat\x12:\n\nhalf_turns\x18\x03 \x01(\x0b\x32&.cirq.google.api.v1.ParameterizedFloat\"m\n\x04\x45xpZ\x12)\n\x06target\x18\x01 \x01(\x0b\x32\x19.cirq.google.api.v1.Qubit\x12:\n\nhalf_turns\x18\x02 \x01(\x0b\x32&.cirq.google.api.v1.ParameterizedFloat\"\x9b\x01\n\x05\x45xp11\x12*\n\x07target1\x18\x01 \x01(\x0b\x32\x19.cirq.google.api.v1.Qubit\x12*\n\x07target2\x18\x02 \x01(\x0b\x32\x19.cirq.google.api.v1.Qubit\x12:\n\nhalf_turns\x18\x03 \x01(\x0b\x32&.cirq.google.api.v1.ParameterizedFloat\"[\n\x0bMeasurement\x12*\n\x07targets\x18\x01 \x03(\x0b\x32\x19.cirq.google.api.v1.Qubit\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x13\n\x0binvert_mask\x18\x03 \x03(\x08\"\xfa\x01\n\tOperation\x12%\n\x1dincremental_delay_picoseconds\x18\x01 \x01(\x04\x12)\n\x05\x65xp_w\x18\n \x01(\x0b\x32\x18.cirq.google.api.v1.ExpWH\x00\x12)\n\x05\x65xp_z\x18\x0b \x01(\x0b\x32\x18.cirq.google.api.v1.ExpZH\x00\x12+\n\x06\x65xp_11\x18\x0c \x01(\x0b\x32\x19.cirq.google.api.v1.Exp11H\x00\x12\x36\n\x0bmeasurement\x18\r \x01(\x0b\x32\x1f.cirq.google.api.v1.MeasurementH\x00\x42\x0b\n\toperationB2\n\x1d\x63om.google.cirq.google.api.v1B\x0fOperationsProtoP\x01\x62\x06proto3')
)




_QUBIT = _descriptor.Descriptor(
  name='Qubit',
  full_name='cirq.google.api.v1.Qubit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='cirq.google.api.v1.Qubit.row', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='col', full_name='cirq.google.api.v1.Qubit.col', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=92,
)


_PARAMETERIZEDFLOAT = _descriptor.Descriptor(
  name='ParameterizedFloat',
  full_name='cirq.google.api.v1.ParameterizedFloat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raw', full_name='cirq.google.api.v1.ParameterizedFloat.raw', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameter_key', full_name='cirq.google.api.v1.ParameterizedFloat.parameter_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='cirq.google.api.v1.ParameterizedFloat.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=94,
  serialized_end=163,
)


_EXPW = _descriptor.Descriptor(
  name='ExpW',
  full_name='cirq.google.api.v1.ExpW',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='cirq.google.api.v1.ExpW.target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='axis_half_turns', full_name='cirq.google.api.v1.ExpW.axis_half_turns', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='half_turns', full_name='cirq.google.api.v1.ExpW.half_turns', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=340,
)


_EXPZ = _descriptor.Descriptor(
  name='ExpZ',
  full_name='cirq.google.api.v1.ExpZ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='cirq.google.api.v1.ExpZ.target', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='half_turns', full_name='cirq.google.api.v1.ExpZ.half_turns', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=451,
)


_EXP11 = _descriptor.Descriptor(
  name='Exp11',
  full_name='cirq.google.api.v1.Exp11',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target1', full_name='cirq.google.api.v1.Exp11.target1', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target2', full_name='cirq.google.api.v1.Exp11.target2', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='half_turns', full_name='cirq.google.api.v1.Exp11.half_turns', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=454,
  serialized_end=609,
)


_MEASUREMENT = _descriptor.Descriptor(
  name='Measurement',
  full_name='cirq.google.api.v1.Measurement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targets', full_name='cirq.google.api.v1.Measurement.targets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='cirq.google.api.v1.Measurement.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='invert_mask', full_name='cirq.google.api.v1.Measurement.invert_mask', index=2,
      number=3, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=611,
  serialized_end=702,
)


_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='cirq.google.api.v1.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='incremental_delay_picoseconds', full_name='cirq.google.api.v1.Operation.incremental_delay_picoseconds', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_w', full_name='cirq.google.api.v1.Operation.exp_w', index=1,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_z', full_name='cirq.google.api.v1.Operation.exp_z', index=2,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exp_11', full_name='cirq.google.api.v1.Operation.exp_11', index=3,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='measurement', full_name='cirq.google.api.v1.Operation.measurement', index=4,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operation', full_name='cirq.google.api.v1.Operation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=705,
  serialized_end=955,
)

_PARAMETERIZEDFLOAT.oneofs_by_name['value'].fields.append(
  _PARAMETERIZEDFLOAT.fields_by_name['raw'])
_PARAMETERIZEDFLOAT.fields_by_name['raw'].containing_oneof = _PARAMETERIZEDFLOAT.oneofs_by_name['value']
_PARAMETERIZEDFLOAT.oneofs_by_name['value'].fields.append(
  _PARAMETERIZEDFLOAT.fields_by_name['parameter_key'])
_PARAMETERIZEDFLOAT.fields_by_name['parameter_key'].containing_oneof = _PARAMETERIZEDFLOAT.oneofs_by_name['value']
_EXPW.fields_by_name['target'].message_type = _QUBIT
_EXPW.fields_by_name['axis_half_turns'].message_type = _PARAMETERIZEDFLOAT
_EXPW.fields_by_name['half_turns'].message_type = _PARAMETERIZEDFLOAT
_EXPZ.fields_by_name['target'].message_type = _QUBIT
_EXPZ.fields_by_name['half_turns'].message_type = _PARAMETERIZEDFLOAT
_EXP11.fields_by_name['target1'].message_type = _QUBIT
_EXP11.fields_by_name['target2'].message_type = _QUBIT
_EXP11.fields_by_name['half_turns'].message_type = _PARAMETERIZEDFLOAT
_MEASUREMENT.fields_by_name['targets'].message_type = _QUBIT
_OPERATION.fields_by_name['exp_w'].message_type = _EXPW
_OPERATION.fields_by_name['exp_z'].message_type = _EXPZ
_OPERATION.fields_by_name['exp_11'].message_type = _EXP11
_OPERATION.fields_by_name['measurement'].message_type = _MEASUREMENT
_OPERATION.oneofs_by_name['operation'].fields.append(
  _OPERATION.fields_by_name['exp_w'])
_OPERATION.fields_by_name['exp_w'].containing_oneof = _OPERATION.oneofs_by_name['operation']
_OPERATION.oneofs_by_name['operation'].fields.append(
  _OPERATION.fields_by_name['exp_z'])
_OPERATION.fields_by_name['exp_z'].containing_oneof = _OPERATION.oneofs_by_name['operation']
_OPERATION.oneofs_by_name['operation'].fields.append(
  _OPERATION.fields_by_name['exp_11'])
_OPERATION.fields_by_name['exp_11'].containing_oneof = _OPERATION.oneofs_by_name['operation']
_OPERATION.oneofs_by_name['operation'].fields.append(
  _OPERATION.fields_by_name['measurement'])
_OPERATION.fields_by_name['measurement'].containing_oneof = _OPERATION.oneofs_by_name['operation']
DESCRIPTOR.message_types_by_name['Qubit'] = _QUBIT
DESCRIPTOR.message_types_by_name['ParameterizedFloat'] = _PARAMETERIZEDFLOAT
DESCRIPTOR.message_types_by_name['ExpW'] = _EXPW
DESCRIPTOR.message_types_by_name['ExpZ'] = _EXPZ
DESCRIPTOR.message_types_by_name['Exp11'] = _EXP11
DESCRIPTOR.message_types_by_name['Measurement'] = _MEASUREMENT
DESCRIPTOR.message_types_by_name['Operation'] = _OPERATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Qubit = _reflection.GeneratedProtocolMessageType('Qubit', (_message.Message,), {
  'DESCRIPTOR' : _QUBIT,
  '__module__' : 'cirq_google.api.v1.operations_pb2'
  # @@protoc_insertion_point(class_scope:cirq.google.api.v1.Qubit)
  })
_sym_db.RegisterMessage(Qubit)

ParameterizedFloat = _reflection.GeneratedProtocolMessageType('ParameterizedFloat', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETERIZEDFLOAT,
  '__module__' : 'cirq_google.api.v1.operations_pb2'
  # @@protoc_insertion_point(class_scope:cirq.google.api.v1.ParameterizedFloat)
  })
_sym_db.RegisterMessage(ParameterizedFloat)

ExpW = _reflection.GeneratedProtocolMessageType('ExpW', (_message.Message,), {
  'DESCRIPTOR' : _EXPW,
  '__module__' : 'cirq_google.api.v1.operations_pb2'
  # @@protoc_insertion_point(class_scope:cirq.google.api.v1.ExpW)
  })
_sym_db.RegisterMessage(ExpW)

ExpZ = _reflection.GeneratedProtocolMessageType('ExpZ', (_message.Message,), {
  'DESCRIPTOR' : _EXPZ,
  '__module__' : 'cirq_google.api.v1.operations_pb2'
  # @@protoc_insertion_point(class_scope:cirq.google.api.v1.ExpZ)
  })
_sym_db.RegisterMessage(ExpZ)

Exp11 = _reflection.GeneratedProtocolMessageType('Exp11', (_message.Message,), {
  'DESCRIPTOR' : _EXP11,
  '__module__' : 'cirq_google.api.v1.operations_pb2'
  # @@protoc_insertion_point(class_scope:cirq.google.api.v1.Exp11)
  })
_sym_db.RegisterMessage(Exp11)

Measurement = _reflection.GeneratedProtocolMessageType('Measurement', (_message.Message,), {
  'DESCRIPTOR' : _MEASUREMENT,
  '__module__' : 'cirq_google.api.v1.operations_pb2'
  # @@protoc_insertion_point(class_scope:cirq.google.api.v1.Measurement)
  })
_sym_db.RegisterMessage(Measurement)

Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), {
  'DESCRIPTOR' : _OPERATION,
  '__module__' : 'cirq_google.api.v1.operations_pb2'
  # @@protoc_insertion_point(class_scope:cirq.google.api.v1.Operation)
  })
_sym_db.RegisterMessage(Operation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
