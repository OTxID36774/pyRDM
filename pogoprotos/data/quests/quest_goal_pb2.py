# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/quests/quest_goal.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.quests import quest_condition_pb2 as pogoprotos_dot_data_dot_quests_dot_quest__condition__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/quests/quest_goal.proto',
  package='pogoprotos.data.quests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'pogoprotos/data/quests/quest_goal.proto\x12\x16pogoprotos.data.quests\x1a,pogoprotos/data/quests/quest_condition.proto\"V\n\tQuestGoal\x12\x39\n\tcondition\x18\x01 \x03(\x0b\x32&.pogoprotos.data.quests.QuestCondition\x12\x0e\n\x06target\x18\x02 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_quests_dot_quest__condition__pb2.DESCRIPTOR,])




_QUESTGOAL = _descriptor.Descriptor(
  name='QuestGoal',
  full_name='pogoprotos.data.quests.QuestGoal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condition', full_name='pogoprotos.data.quests.QuestGoal.condition', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target', full_name='pogoprotos.data.quests.QuestGoal.target', index=1,
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
  serialized_start=113,
  serialized_end=199,
)

_QUESTGOAL.fields_by_name['condition'].message_type = pogoprotos_dot_data_dot_quests_dot_quest__condition__pb2._QUESTCONDITION
DESCRIPTOR.message_types_by_name['QuestGoal'] = _QUESTGOAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuestGoal = _reflection.GeneratedProtocolMessageType('QuestGoal', (_message.Message,), dict(
  DESCRIPTOR = _QUESTGOAL,
  __module__ = 'pogoprotos.data.quests.quest_goal_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.QuestGoal)
  ))
_sym_db.RegisterMessage(QuestGoal)


# @@protoc_insertion_point(module_scope)
