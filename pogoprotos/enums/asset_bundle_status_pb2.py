# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/asset_bundle_status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/asset_bundle_status.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n*pogoprotos/enums/asset_bundle_status.proto\x12\x10pogoprotos.enums*Z\n\x11\x41ssetBundleStatus\x12\x0c\n\x08UNLOADED\x10\x00\x12\x0b\n\x07LOADING\x10\x01\x12\n\n\x06LOADED\x10\x02\x12\x1e\n\x1a\x46\x41ILED_ASSET_BUNDLE_STATUS\x10\x03\x62\x06proto3')
)

_ASSETBUNDLESTATUS = _descriptor.EnumDescriptor(
  name='AssetBundleStatus',
  full_name='pogoprotos.enums.AssetBundleStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNLOADED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOADING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOADED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED_ASSET_BUNDLE_STATUS', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=64,
  serialized_end=154,
)
_sym_db.RegisterEnumDescriptor(_ASSETBUNDLESTATUS)

AssetBundleStatus = enum_type_wrapper.EnumTypeWrapper(_ASSETBUNDLESTATUS)
UNLOADED = 0
LOADING = 1
LOADED = 2
FAILED_ASSET_BUNDLE_STATUS = 3


DESCRIPTOR.enum_types_by_name['AssetBundleStatus'] = _ASSETBUNDLESTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
