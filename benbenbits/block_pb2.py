# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: block.proto

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
  name='block.proto',
  package='',
  serialized_pb=_b('\n\x0b\x62lock.proto\"P\n\x0bTransaction\x12\x0e\n\x06sender\x18\x01 \x02(\x0c\x12\x0e\n\x06recver\x18\x02 \x02(\x0c\x12\x0e\n\x06\x61mount\x18\x03 \x02(\x04\x12\x11\n\tsignature\x18\x04 \x02(\x0c\"|\n\rBlockContents\x12\x1a\n\x04txns\x18\x01 \x03(\x0b\x32\x0c.Transaction\x12\x0c\n\x04time\x18\x02 \x02(\r\x12\x10\n\x08prevHash\x18\x03 \x02(\x0c\x12\x10\n\x08nextDiff\x18\x04 \x02(\x04\x12\x0b\n\x03num\x18\x05 \x02(\r\x12\x10\n\x08thisDiff\x18\x06 \x02(\x04\"e\n\x05\x42lock\x12\x1c\n\x04\x63nts\x18\x01 \x02(\x0b\x32\x0e.BlockContents\x12\x11\n\tsignature\x18\x02 \x02(\x0c\x12\x0c\n\x04hash\x18\x03 \x02(\x0c\x12\r\n\x05nonce\x18\x04 \x02(\x04\x12\x0e\n\x06pubkey\x18\x05 \x02(\x0c')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='Transaction.sender', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recver', full_name='Transaction.recver', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='Transaction.amount', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='Transaction.signature', index=3,
      number=4, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=95,
)


_BLOCKCONTENTS = _descriptor.Descriptor(
  name='BlockContents',
  full_name='BlockContents',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txns', full_name='BlockContents.txns', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='BlockContents.time', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='prevHash', full_name='BlockContents.prevHash', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nextDiff', full_name='BlockContents.nextDiff', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num', full_name='BlockContents.num', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thisDiff', full_name='BlockContents.thisDiff', index=5,
      number=6, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=221,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cnts', full_name='Block.cnts', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='Block.signature', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hash', full_name='Block.hash', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='Block.nonce', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pubkey', full_name='Block.pubkey', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=223,
  serialized_end=324,
)

_BLOCKCONTENTS.fields_by_name['txns'].message_type = _TRANSACTION
_BLOCK.fields_by_name['cnts'].message_type = _BLOCKCONTENTS
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['BlockContents'] = _BLOCKCONTENTS
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

BlockContents = _reflection.GeneratedProtocolMessageType('BlockContents', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKCONTENTS,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:BlockContents)
  ))
_sym_db.RegisterMessage(BlockContents)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'block_pb2'
  # @@protoc_insertion_point(class_scope:Block)
  ))
_sym_db.RegisterMessage(Block)


# @@protoc_insertion_point(module_scope)
