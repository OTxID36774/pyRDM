# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/map/fort/gym_display.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.map.fort import gym_event_pb2 as pogoprotos_dot_map_dot_fort_dot_gym__event__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/map/fort/gym_display.proto',
  package='pogoprotos.map.fort',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n%pogoprotos/map/fort/gym_display.proto\x12\x13pogoprotos.map.fort\x1a#pogoprotos/map/fort/gym_event.proto\"\xa9\x01\n\nGymDisplay\x12\x30\n\tgym_event\x18\x01 \x03(\x0b\x32\x1d.pogoprotos.map.fort.GymEvent\x12\x14\n\x0ctotal_gym_cp\x18\x02 \x01(\x05\x12!\n\x19lowest_pokemon_motivation\x18\x03 \x01(\x01\x12\x17\n\x0fslots_available\x18\x04 \x01(\x05\x12\x17\n\x0foccupied_millis\x18\x05 \x01(\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_map_dot_fort_dot_gym__event__pb2.DESCRIPTOR,])




_GYMDISPLAY = _descriptor.Descriptor(
  name='GymDisplay',
  full_name='pogoprotos.map.fort.GymDisplay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gym_event', full_name='pogoprotos.map.fort.GymDisplay.gym_event', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_gym_cp', full_name='pogoprotos.map.fort.GymDisplay.total_gym_cp', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lowest_pokemon_motivation', full_name='pogoprotos.map.fort.GymDisplay.lowest_pokemon_motivation', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slots_available', full_name='pogoprotos.map.fort.GymDisplay.slots_available', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occupied_millis', full_name='pogoprotos.map.fort.GymDisplay.occupied_millis', index=4,
      number=5, type=3, cpp_type=2, label=1,
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
  serialized_start=100,
  serialized_end=269,
)

_GYMDISPLAY.fields_by_name['gym_event'].message_type = pogoprotos_dot_map_dot_fort_dot_gym__event__pb2._GYMEVENT
DESCRIPTOR.message_types_by_name['GymDisplay'] = _GYMDISPLAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GymDisplay = _reflection.GeneratedProtocolMessageType('GymDisplay', (_message.Message,), dict(
  DESCRIPTOR = _GYMDISPLAY,
  __module__ = 'pogoprotos.map.fort.gym_display_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.map.fort.GymDisplay)
  ))
_sym_db.RegisterMessage(GymDisplay)


# @@protoc_insertion_point(module_scope)