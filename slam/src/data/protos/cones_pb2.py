# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cones.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cones.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x63ones.proto\"6\n\x04\x43one\x12\x10\n\x08\x64istance\x18\x01 \x01(\x02\x12\r\n\x05\x61ngle\x18\x02 \x01(\x02\x12\r\n\x05width\x18\x03 \x01(\x02\" \n\x08\x43oneList\x12\x14\n\x05\x63ones\x18\x01 \x03(\x0b\x32\x05.Coneb\x06proto3'
)




_CONE = _descriptor.Descriptor(
  name='Cone',
  full_name='Cone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='distance', full_name='Cone.distance', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='angle', full_name='Cone.angle', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='Cone.width', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=15,
  serialized_end=69,
)


_CONELIST = _descriptor.Descriptor(
  name='ConeList',
  full_name='ConeList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cones', full_name='ConeList.cones', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=71,
  serialized_end=103,
)

_CONELIST.fields_by_name['cones'].message_type = _CONE
DESCRIPTOR.message_types_by_name['Cone'] = _CONE
DESCRIPTOR.message_types_by_name['ConeList'] = _CONELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Cone = _reflection.GeneratedProtocolMessageType('Cone', (_message.Message,), {
  'DESCRIPTOR' : _CONE,
  '__module__' : 'cones_pb2'
  # @@protoc_insertion_point(class_scope:Cone)
  })
_sym_db.RegisterMessage(Cone)

ConeList = _reflection.GeneratedProtocolMessageType('ConeList', (_message.Message,), {
  'DESCRIPTOR' : _CONELIST,
  '__module__' : 'cones_pb2'
  # @@protoc_insertion_point(class_scope:ConeList)
  })
_sym_db.RegisterMessage(ConeList)


# @@protoc_insertion_point(module_scope)
