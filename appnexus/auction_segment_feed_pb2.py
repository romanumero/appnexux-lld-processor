# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auction_segment_feed.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import includes.segment_key_value_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='auction_segment_feed.proto',
  package='',
  serialized_pb='\n\x1a\x61uction_segment_feed.proto\x1a includes/segment_key_value.proto\"\xce\x01\n\x14\x61uction_segment_feed\x12\x11\n\tdate_time\x18\x01 \x01(\x06\x12\x15\n\rauction_id_64\x18\x02 \x01(\x06\x12\x12\n\nuser_id_64\x18\x03 \x01(\x06\x12\x18\n\x10seller_member_id\x18\x04 \x01(\x05\x12$\n\x08segments\x18\x05 \x03(\x0b\x32\x12.segment_key_value\x12\x19\n\x11hashed_user_id_64\x18\x06 \x01(\x0c\x12\x1d\n\x15partition_time_millis\x18\x07 \x01(\x06\x42&\n$com.appnexus.data.protobuf.generated')




_AUCTION_SEGMENT_FEED = _descriptor.Descriptor(
  name='auction_segment_feed',
  full_name='auction_segment_feed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date_time', full_name='auction_segment_feed.date_time', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auction_id_64', full_name='auction_segment_feed.auction_id_64', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id_64', full_name='auction_segment_feed.user_id_64', index=2,
      number=3, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seller_member_id', full_name='auction_segment_feed.seller_member_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='segments', full_name='auction_segment_feed.segments', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hashed_user_id_64', full_name='auction_segment_feed.hashed_user_id_64', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='partition_time_millis', full_name='auction_segment_feed.partition_time_millis', index=6,
      number=7, type=6, cpp_type=4, label=1,
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
  serialized_start=65,
  serialized_end=271,
)

_AUCTION_SEGMENT_FEED.fields_by_name['segments'].message_type = includes.segment_key_value_pb2._SEGMENT_KEY_VALUE
DESCRIPTOR.message_types_by_name['auction_segment_feed'] = _AUCTION_SEGMENT_FEED

class auction_segment_feed(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _AUCTION_SEGMENT_FEED

  # @@protoc_insertion_point(class_scope:auction_segment_feed)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n$com.appnexus.data.protobuf.generated')
# @@protoc_insertion_point(module_scope)
