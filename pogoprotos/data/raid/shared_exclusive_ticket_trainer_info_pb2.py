# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/raid/shared_exclusive_ticket_trainer_info.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/raid/shared_exclusive_ticket_trainer_info.proto',
  package='pogoprotos.data.raid',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n?pogoprotos/data/raid/shared_exclusive_ticket_trainer_info.proto\x12\x14pogoprotos.data.raid\"G\n SharedExclusiveTicketTrainerInfo\x12\x10\n\x08\x63odename\x18\x01 \x01(\t\x12\x11\n\tplayer_id\x18\x02 \x01(\tb\x06proto3')
)




_SHAREDEXCLUSIVETICKETTRAINERINFO = _descriptor.Descriptor(
  name='SharedExclusiveTicketTrainerInfo',
  full_name='pogoprotos.data.raid.SharedExclusiveTicketTrainerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='codename', full_name='pogoprotos.data.raid.SharedExclusiveTicketTrainerInfo.codename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_id', full_name='pogoprotos.data.raid.SharedExclusiveTicketTrainerInfo.player_id', index=1,
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
  ],
  serialized_start=89,
  serialized_end=160,
)

DESCRIPTOR.message_types_by_name['SharedExclusiveTicketTrainerInfo'] = _SHAREDEXCLUSIVETICKETTRAINERINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SharedExclusiveTicketTrainerInfo = _reflection.GeneratedProtocolMessageType('SharedExclusiveTicketTrainerInfo', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDEXCLUSIVETICKETTRAINERINFO,
  __module__ = 'pogoprotos.data.raid.shared_exclusive_ticket_trainer_info_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.raid.SharedExclusiveTicketTrainerInfo)
  ))
_sym_db.RegisterMessage(SharedExclusiveTicketTrainerInfo)


# @@protoc_insertion_point(module_scope)
