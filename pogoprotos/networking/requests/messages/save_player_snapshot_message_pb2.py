# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/save_player_snapshot_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/save_player_snapshot_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nJpogoprotos/networking/requests/messages/save_player_snapshot_message.proto\x12\'pogoprotos.networking.requests.messages\"\x1b\n\x19SavePlayerSnapshotMessageb\x06proto3')
)




_SAVEPLAYERSNAPSHOTMESSAGE = _descriptor.Descriptor(
  name='SavePlayerSnapshotMessage',
  full_name='pogoprotos.networking.requests.messages.SavePlayerSnapshotMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=119,
  serialized_end=146,
)

DESCRIPTOR.message_types_by_name['SavePlayerSnapshotMessage'] = _SAVEPLAYERSNAPSHOTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SavePlayerSnapshotMessage = _reflection.GeneratedProtocolMessageType('SavePlayerSnapshotMessage', (_message.Message,), dict(
  DESCRIPTOR = _SAVEPLAYERSNAPSHOTMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.save_player_snapshot_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.SavePlayerSnapshotMessage)
  ))
_sym_db.RegisterMessage(SavePlayerSnapshotMessage)


# @@protoc_insertion_point(module_scope)
