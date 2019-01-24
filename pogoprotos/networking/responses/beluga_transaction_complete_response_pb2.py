# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/beluga_transaction_complete_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.inventory import loot_pb2 as pogoprotos_dot_inventory_dot_loot__pb2
from pogoprotos.data.beluga import beluga_ble_finalize_transfer_pb2 as pogoprotos_dot_data_dot_beluga_dot_beluga__ble__finalize__transfer__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/beluga_transaction_complete_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nJpogoprotos/networking/responses/beluga_transaction_complete_response.proto\x12\x1fpogoprotos.networking.responses\x1a\x1fpogoprotos/inventory/loot.proto\x1a\x39pogoprotos/data/beluga/beluga_ble_finalize_transfer.proto\"\xa8\x04\n!BelugaTransactionCompleteResponse\x12Y\n\x06status\x18\x01 \x01(\x0e\x32I.pogoprotos.networking.responses.BelugaTransactionCompleteResponse.Status\x12\x15\n\rcandy_awarded\x18\x02 \x01(\x05\x12\x30\n\x0cloot_awarded\x18\x03 \x01(\x0b\x32\x1a.pogoprotos.inventory.Loot\x12S\n\x18\x62\x65luga_finalize_response\x18\x04 \x01(\x0b\x32\x31.pogoprotos.data.beluga.BelugaBleFinalizeTransfer\x12\"\n\x1a\x62uckets_until_weekly_award\x18\x05 \x01(\x05\"\xe5\x01\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\x12\x1c\n\x18\x45RROR_INVALID_POKEMON_ID\x10\x03\x12\x1a\n\x16\x45RROR_POKEMON_DEPLOYED\x10\x04\x12\x1d\n\x19\x45RROR_POKEMON_NOT_ALLOWED\x10\x05\x12\x1a\n\x16\x45RROR_POKEMON_IS_BUDDY\x10\x06\x12 \n\x1c\x45RROR_INVALID_TRANSACTION_ID\x10\x07\x12 \n\x1c\x45RROR_MISSING_TRANSACTION_ID\x10\x08\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_inventory_dot_loot__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_beluga_dot_beluga__ble__finalize__transfer__pb2.DESCRIPTOR,])



_BELUGATRANSACTIONCOMPLETERESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='pogoprotos.networking.responses.BelugaTransactionCompleteResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_POKEMON_ID', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_DEPLOYED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_NOT_ALLOWED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_IS_BUDDY', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_INVALID_TRANSACTION_ID', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_MISSING_TRANSACTION_ID', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=527,
  serialized_end=756,
)
_sym_db.RegisterEnumDescriptor(_BELUGATRANSACTIONCOMPLETERESPONSE_STATUS)


_BELUGATRANSACTIONCOMPLETERESPONSE = _descriptor.Descriptor(
  name='BelugaTransactionCompleteResponse',
  full_name='pogoprotos.networking.responses.BelugaTransactionCompleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='pogoprotos.networking.responses.BelugaTransactionCompleteResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='candy_awarded', full_name='pogoprotos.networking.responses.BelugaTransactionCompleteResponse.candy_awarded', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loot_awarded', full_name='pogoprotos.networking.responses.BelugaTransactionCompleteResponse.loot_awarded', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beluga_finalize_response', full_name='pogoprotos.networking.responses.BelugaTransactionCompleteResponse.beluga_finalize_response', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buckets_until_weekly_award', full_name='pogoprotos.networking.responses.BelugaTransactionCompleteResponse.buckets_until_weekly_award', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BELUGATRANSACTIONCOMPLETERESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=204,
  serialized_end=756,
)

_BELUGATRANSACTIONCOMPLETERESPONSE.fields_by_name['status'].enum_type = _BELUGATRANSACTIONCOMPLETERESPONSE_STATUS
_BELUGATRANSACTIONCOMPLETERESPONSE.fields_by_name['loot_awarded'].message_type = pogoprotos_dot_inventory_dot_loot__pb2._LOOT
_BELUGATRANSACTIONCOMPLETERESPONSE.fields_by_name['beluga_finalize_response'].message_type = pogoprotos_dot_data_dot_beluga_dot_beluga__ble__finalize__transfer__pb2._BELUGABLEFINALIZETRANSFER
_BELUGATRANSACTIONCOMPLETERESPONSE_STATUS.containing_type = _BELUGATRANSACTIONCOMPLETERESPONSE
DESCRIPTOR.message_types_by_name['BelugaTransactionCompleteResponse'] = _BELUGATRANSACTIONCOMPLETERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BelugaTransactionCompleteResponse = _reflection.GeneratedProtocolMessageType('BelugaTransactionCompleteResponse', (_message.Message,), dict(
  DESCRIPTOR = _BELUGATRANSACTIONCOMPLETERESPONSE,
  __module__ = 'pogoprotos.networking.responses.beluga_transaction_complete_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.BelugaTransactionCompleteResponse)
  ))
_sym_db.RegisterMessage(BelugaTransactionCompleteResponse)


# @@protoc_insertion_point(module_scope)
