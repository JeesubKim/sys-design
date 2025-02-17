# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: location.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'location.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0elocation.proto\x12\x08location\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\"$\n\x08Location\x12\x0b\n\x03lat\x18\x01 \x01(\t\x12\x0b\n\x03lng\x18\x02 \x01(\t\"-\n\x18GetDriverLocationRequest\x12\x11\n\tdriver_id\x18\x01 \x01(\x03\")\n\x16GetUserLocationRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\"[\n\x15UpdateLocationRequest\x12\x0e\n\x06parent\x18\x01 \x01(\x03\x12\x0c\n\x04type\x18\x02 \x01(\t\x12$\n\x08location\x18\x03 \x01(\x0b\x32\x12.location.Location2\xe5\x02\n\x0fLocationService\x12p\n\x0fgetUserLocation\x12 .location.GetUserLocationRequest\x1a\x12.location.Location\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/api/v1/location/user/{user_id}\x12x\n\x11getDriverLocation\x12\".location.GetDriverLocationRequest\x1a\x12.location.Location\"+\x82\xd3\xe4\x93\x02%\x12#/api/v1/location/driver/{driver_id}\x12\x66\n\x0eupdateLocation\x12\x1f.location.UpdateLocationRequest\x1a\x16.google.protobuf.Empty\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/api/v1/location:\x01*B\x16Z\x14grpc-gw/api/locationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'location_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\024grpc-gw/api/location'
  _globals['_LOCATIONSERVICE'].methods_by_name['getUserLocation']._loaded_options = None
  _globals['_LOCATIONSERVICE'].methods_by_name['getUserLocation']._serialized_options = b'\202\323\344\223\002!\022\037/api/v1/location/user/{user_id}'
  _globals['_LOCATIONSERVICE'].methods_by_name['getDriverLocation']._loaded_options = None
  _globals['_LOCATIONSERVICE'].methods_by_name['getDriverLocation']._serialized_options = b'\202\323\344\223\002%\022#/api/v1/location/driver/{driver_id}'
  _globals['_LOCATIONSERVICE'].methods_by_name['updateLocation']._loaded_options = None
  _globals['_LOCATIONSERVICE'].methods_by_name['updateLocation']._serialized_options = b'\202\323\344\223\002\025\"\020/api/v1/location:\001*'
  _globals['_LOCATION']._serialized_start=87
  _globals['_LOCATION']._serialized_end=123
  _globals['_GETDRIVERLOCATIONREQUEST']._serialized_start=125
  _globals['_GETDRIVERLOCATIONREQUEST']._serialized_end=170
  _globals['_GETUSERLOCATIONREQUEST']._serialized_start=172
  _globals['_GETUSERLOCATIONREQUEST']._serialized_end=213
  _globals['_UPDATELOCATIONREQUEST']._serialized_start=215
  _globals['_UPDATELOCATIONREQUEST']._serialized_end=306
  _globals['_LOCATIONSERVICE']._serialized_start=309
  _globals['_LOCATIONSERVICE']._serialized_end=666
# @@protoc_insertion_point(module_scope)
