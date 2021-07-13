"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class HashOp(metaclass=_HashOp):
    V = typing.NewType('V', builtins.int)

global___HashOp = HashOp

NO_HASH = HashOp.V(0)
SHA256 = HashOp.V(1)
SHA512 = HashOp.V(2)
KECCAK = HashOp.V(3)
RIPEMD160 = HashOp.V(4)
BITCOIN = HashOp.V(5)

class _HashOp(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[HashOp.V], builtins.type):  # type: ignore
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    NO_HASH = HashOp.V(0)
    SHA256 = HashOp.V(1)
    SHA512 = HashOp.V(2)
    KECCAK = HashOp.V(3)
    RIPEMD160 = HashOp.V(4)
    BITCOIN = HashOp.V(5)

class LengthOp(metaclass=_LengthOp):
    V = typing.NewType('V', builtins.int)

global___LengthOp = LengthOp

NO_PREFIX = LengthOp.V(0)
VAR_PROTO = LengthOp.V(1)
VAR_RLP = LengthOp.V(2)
FIXED32_BIG = LengthOp.V(3)
FIXED32_LITTLE = LengthOp.V(4)
FIXED64_BIG = LengthOp.V(5)
FIXED64_LITTLE = LengthOp.V(6)
REQUIRE_32_BYTES = LengthOp.V(7)
REQUIRE_64_BYTES = LengthOp.V(8)

class _LengthOp(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LengthOp.V], builtins.type):  # type: ignore
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    NO_PREFIX = LengthOp.V(0)
    VAR_PROTO = LengthOp.V(1)
    VAR_RLP = LengthOp.V(2)
    FIXED32_BIG = LengthOp.V(3)
    FIXED32_LITTLE = LengthOp.V(4)
    FIXED64_BIG = LengthOp.V(5)
    FIXED64_LITTLE = LengthOp.V(6)
    REQUIRE_32_BYTES = LengthOp.V(7)
    REQUIRE_64_BYTES = LengthOp.V(8)

class ExistenceProof(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    LEAF_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    key: builtins.bytes = ...
    value: builtins.bytes = ...

    @property
    def leaf(self) -> global___LeafOp: ...

    @property
    def path(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InnerOp]: ...

    def __init__(self,
        *,
        key : builtins.bytes = ...,
        value : builtins.bytes = ...,
        leaf : typing.Optional[global___LeafOp] = ...,
        path : typing.Optional[typing.Iterable[global___InnerOp]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"leaf",b"leaf"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"leaf",b"leaf",u"path",b"path",u"value",b"value"]) -> None: ...
global___ExistenceProof = ExistenceProof

class NonExistenceProof(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_FIELD_NUMBER: builtins.int
    LEFT_FIELD_NUMBER: builtins.int
    RIGHT_FIELD_NUMBER: builtins.int
    key: builtins.bytes = ...

    @property
    def left(self) -> global___ExistenceProof: ...

    @property
    def right(self) -> global___ExistenceProof: ...

    def __init__(self,
        *,
        key : builtins.bytes = ...,
        left : typing.Optional[global___ExistenceProof] = ...,
        right : typing.Optional[global___ExistenceProof] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"left",b"left",u"right",b"right"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"left",b"left",u"right",b"right"]) -> None: ...
global___NonExistenceProof = NonExistenceProof

class CommitmentProof(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EXIST_FIELD_NUMBER: builtins.int
    NONEXIST_FIELD_NUMBER: builtins.int
    BATCH_FIELD_NUMBER: builtins.int
    COMPRESSED_FIELD_NUMBER: builtins.int

    @property
    def exist(self) -> global___ExistenceProof: ...

    @property
    def nonexist(self) -> global___NonExistenceProof: ...

    @property
    def batch(self) -> global___BatchProof: ...

    @property
    def compressed(self) -> global___CompressedBatchProof: ...

    def __init__(self,
        *,
        exist : typing.Optional[global___ExistenceProof] = ...,
        nonexist : typing.Optional[global___NonExistenceProof] = ...,
        batch : typing.Optional[global___BatchProof] = ...,
        compressed : typing.Optional[global___CompressedBatchProof] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"batch",b"batch",u"compressed",b"compressed",u"exist",b"exist",u"nonexist",b"nonexist",u"proof",b"proof"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"batch",b"batch",u"compressed",b"compressed",u"exist",b"exist",u"nonexist",b"nonexist",u"proof",b"proof"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"proof",b"proof"]) -> typing.Optional[typing_extensions.Literal["exist","nonexist","batch","compressed"]]: ...
global___CommitmentProof = CommitmentProof

class LeafOp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HASH_FIELD_NUMBER: builtins.int
    PREHASH_KEY_FIELD_NUMBER: builtins.int
    PREHASH_VALUE_FIELD_NUMBER: builtins.int
    LENGTH_FIELD_NUMBER: builtins.int
    PREFIX_FIELD_NUMBER: builtins.int
    hash: global___HashOp.V = ...
    prehash_key: global___HashOp.V = ...
    prehash_value: global___HashOp.V = ...
    length: global___LengthOp.V = ...
    prefix: builtins.bytes = ...

    def __init__(self,
        *,
        hash : global___HashOp.V = ...,
        prehash_key : global___HashOp.V = ...,
        prehash_value : global___HashOp.V = ...,
        length : global___LengthOp.V = ...,
        prefix : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"hash",b"hash",u"length",b"length",u"prefix",b"prefix",u"prehash_key",b"prehash_key",u"prehash_value",b"prehash_value"]) -> None: ...
global___LeafOp = LeafOp

class InnerOp(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HASH_FIELD_NUMBER: builtins.int
    PREFIX_FIELD_NUMBER: builtins.int
    SUFFIX_FIELD_NUMBER: builtins.int
    hash: global___HashOp.V = ...
    prefix: builtins.bytes = ...
    suffix: builtins.bytes = ...

    def __init__(self,
        *,
        hash : global___HashOp.V = ...,
        prefix : builtins.bytes = ...,
        suffix : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"hash",b"hash",u"prefix",b"prefix",u"suffix",b"suffix"]) -> None: ...
global___InnerOp = InnerOp

class ProofSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LEAF_SPEC_FIELD_NUMBER: builtins.int
    INNER_SPEC_FIELD_NUMBER: builtins.int
    MAX_DEPTH_FIELD_NUMBER: builtins.int
    MIN_DEPTH_FIELD_NUMBER: builtins.int
    max_depth: builtins.int = ...
    min_depth: builtins.int = ...

    @property
    def leaf_spec(self) -> global___LeafOp: ...

    @property
    def inner_spec(self) -> global___InnerSpec: ...

    def __init__(self,
        *,
        leaf_spec : typing.Optional[global___LeafOp] = ...,
        inner_spec : typing.Optional[global___InnerSpec] = ...,
        max_depth : builtins.int = ...,
        min_depth : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"inner_spec",b"inner_spec",u"leaf_spec",b"leaf_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"inner_spec",b"inner_spec",u"leaf_spec",b"leaf_spec",u"max_depth",b"max_depth",u"min_depth",b"min_depth"]) -> None: ...
global___ProofSpec = ProofSpec

class InnerSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CHILD_ORDER_FIELD_NUMBER: builtins.int
    CHILD_SIZE_FIELD_NUMBER: builtins.int
    MIN_PREFIX_LENGTH_FIELD_NUMBER: builtins.int
    MAX_PREFIX_LENGTH_FIELD_NUMBER: builtins.int
    EMPTY_CHILD_FIELD_NUMBER: builtins.int
    HASH_FIELD_NUMBER: builtins.int

    @property
    def child_order(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    child_size: builtins.int = ...
    min_prefix_length: builtins.int = ...
    max_prefix_length: builtins.int = ...
    empty_child: builtins.bytes = ...
    hash: global___HashOp.V = ...

    def __init__(self,
        *,
        child_order : typing.Optional[typing.Iterable[builtins.int]] = ...,
        child_size : builtins.int = ...,
        min_prefix_length : builtins.int = ...,
        max_prefix_length : builtins.int = ...,
        empty_child : builtins.bytes = ...,
        hash : global___HashOp.V = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"child_order",b"child_order",u"child_size",b"child_size",u"empty_child",b"empty_child",u"hash",b"hash",u"max_prefix_length",b"max_prefix_length",u"min_prefix_length",b"min_prefix_length"]) -> None: ...
global___InnerSpec = InnerSpec

class BatchProof(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENTRIES_FIELD_NUMBER: builtins.int

    @property
    def entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___BatchEntry]: ...

    def __init__(self,
        *,
        entries : typing.Optional[typing.Iterable[global___BatchEntry]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"entries",b"entries"]) -> None: ...
global___BatchProof = BatchProof

class BatchEntry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EXIST_FIELD_NUMBER: builtins.int
    NONEXIST_FIELD_NUMBER: builtins.int

    @property
    def exist(self) -> global___ExistenceProof: ...

    @property
    def nonexist(self) -> global___NonExistenceProof: ...

    def __init__(self,
        *,
        exist : typing.Optional[global___ExistenceProof] = ...,
        nonexist : typing.Optional[global___NonExistenceProof] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"exist",b"exist",u"nonexist",b"nonexist",u"proof",b"proof"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"exist",b"exist",u"nonexist",b"nonexist",u"proof",b"proof"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"proof",b"proof"]) -> typing.Optional[typing_extensions.Literal["exist","nonexist"]]: ...
global___BatchEntry = BatchEntry

class CompressedBatchProof(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ENTRIES_FIELD_NUMBER: builtins.int
    LOOKUP_INNERS_FIELD_NUMBER: builtins.int

    @property
    def entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___CompressedBatchEntry]: ...

    @property
    def lookup_inners(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InnerOp]: ...

    def __init__(self,
        *,
        entries : typing.Optional[typing.Iterable[global___CompressedBatchEntry]] = ...,
        lookup_inners : typing.Optional[typing.Iterable[global___InnerOp]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"entries",b"entries",u"lookup_inners",b"lookup_inners"]) -> None: ...
global___CompressedBatchProof = CompressedBatchProof

class CompressedBatchEntry(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EXIST_FIELD_NUMBER: builtins.int
    NONEXIST_FIELD_NUMBER: builtins.int

    @property
    def exist(self) -> global___CompressedExistenceProof: ...

    @property
    def nonexist(self) -> global___CompressedNonExistenceProof: ...

    def __init__(self,
        *,
        exist : typing.Optional[global___CompressedExistenceProof] = ...,
        nonexist : typing.Optional[global___CompressedNonExistenceProof] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"exist",b"exist",u"nonexist",b"nonexist",u"proof",b"proof"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"exist",b"exist",u"nonexist",b"nonexist",u"proof",b"proof"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"proof",b"proof"]) -> typing.Optional[typing_extensions.Literal["exist","nonexist"]]: ...
global___CompressedBatchEntry = CompressedBatchEntry

class CompressedExistenceProof(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    LEAF_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    key: builtins.bytes = ...
    value: builtins.bytes = ...

    @property
    def path(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...

    @property
    def leaf(self) -> global___LeafOp: ...

    def __init__(self,
        *,
        key : builtins.bytes = ...,
        value : builtins.bytes = ...,
        leaf : typing.Optional[global___LeafOp] = ...,
        path : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"leaf",b"leaf"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"leaf",b"leaf",u"path",b"path",u"value",b"value"]) -> None: ...
global___CompressedExistenceProof = CompressedExistenceProof

class CompressedNonExistenceProof(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_FIELD_NUMBER: builtins.int
    LEFT_FIELD_NUMBER: builtins.int
    RIGHT_FIELD_NUMBER: builtins.int
    key: builtins.bytes = ...

    @property
    def left(self) -> global___CompressedExistenceProof: ...

    @property
    def right(self) -> global___CompressedExistenceProof: ...

    def __init__(self,
        *,
        key : builtins.bytes = ...,
        left : typing.Optional[global___CompressedExistenceProof] = ...,
        right : typing.Optional[global___CompressedExistenceProof] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"left",b"left",u"right",b"right"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"left",b"left",u"right",b"right"]) -> None: ...
global___CompressedNonExistenceProof = CompressedNonExistenceProof
