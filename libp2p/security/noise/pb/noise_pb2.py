# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: libp2p/security/noise/pb/noise.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='libp2p/security/noise/pb/noise.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n$libp2p/security/noise/pb/noise.proto\"Q\n\x15NoiseHandshakePayload\x12\x14\n\x0cidentity_key\x18\x01 \x01(\x0c\x12\x14\n\x0cidentity_sig\x18\x02 \x01(\x0c\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c')
)




_NOISEHANDSHAKEPAYLOAD = _descriptor.Descriptor(
  name='NoiseHandshakePayload',
  full_name='NoiseHandshakePayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity_key', full_name='NoiseHandshakePayload.identity_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identity_sig', full_name='NoiseHandshakePayload.identity_sig', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='NoiseHandshakePayload.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=121,
)

DESCRIPTOR.message_types_by_name['NoiseHandshakePayload'] = _NOISEHANDSHAKEPAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NoiseHandshakePayload = _reflection.GeneratedProtocolMessageType('NoiseHandshakePayload', (_message.Message,), dict(
  DESCRIPTOR = _NOISEHANDSHAKEPAYLOAD,
  __module__ = 'libp2p.security.noise.pb.noise_pb2'
  # @@protoc_insertion_point(class_scope:NoiseHandshakePayload)
  ))
_sym_db.RegisterMessage(NoiseHandshakePayload)


# @@protoc_insertion_point(module_scope)