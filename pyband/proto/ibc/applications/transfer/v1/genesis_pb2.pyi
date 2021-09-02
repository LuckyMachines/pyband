"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import ibc.applications.transfer.v1.transfer_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# GenesisState defines the ibc-transfer genesis state
class GenesisState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PORT_ID_FIELD_NUMBER: builtins.int
    DENOM_TRACES_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    port_id: typing.Text = ...
    @property
    def denom_traces(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ibc.applications.transfer.v1.transfer_pb2.DenomTrace]: ...
    @property
    def params(self) -> ibc.applications.transfer.v1.transfer_pb2.Params: ...
    def __init__(self,
        *,
        port_id : typing.Text = ...,
        denom_traces : typing.Optional[typing.Iterable[ibc.applications.transfer.v1.transfer_pb2.DenomTrace]] = ...,
        params : typing.Optional[ibc.applications.transfer.v1.transfer_pb2.Params] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"denom_traces",b"denom_traces",u"params",b"params",u"port_id",b"port_id"]) -> None: ...
global___GenesisState = GenesisState
