"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.mint.v1beta1.mint_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GenesisState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MINTER_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int

    @property
    def minter(self) -> cosmos.mint.v1beta1.mint_pb2.Minter: ...

    @property
    def params(self) -> cosmos.mint.v1beta1.mint_pb2.Params: ...

    def __init__(self,
        *,
        minter : typing.Optional[cosmos.mint.v1beta1.mint_pb2.Minter] = ...,
        params : typing.Optional[cosmos.mint.v1beta1.mint_pb2.Params] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"minter",b"minter",u"params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"minter",b"minter",u"params",b"params"]) -> None: ...
global___GenesisState = GenesisState
