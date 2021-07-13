"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import ibc.core.client.v1.client_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GenesisState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLIENTS_FIELD_NUMBER: builtins.int
    CLIENTS_CONSENSUS_FIELD_NUMBER: builtins.int
    CLIENTS_METADATA_FIELD_NUMBER: builtins.int
    PARAMS_FIELD_NUMBER: builtins.int
    CREATE_LOCALHOST_FIELD_NUMBER: builtins.int
    NEXT_CLIENT_SEQUENCE_FIELD_NUMBER: builtins.int
    create_localhost: builtins.bool = ...
    next_client_sequence: builtins.int = ...

    @property
    def clients(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ibc.core.client.v1.client_pb2.IdentifiedClientState]: ...

    @property
    def clients_consensus(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ibc.core.client.v1.client_pb2.ClientConsensusStates]: ...

    @property
    def clients_metadata(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___IdentifiedGenesisMetadata]: ...

    @property
    def params(self) -> ibc.core.client.v1.client_pb2.Params: ...

    def __init__(self,
        *,
        clients : typing.Optional[typing.Iterable[ibc.core.client.v1.client_pb2.IdentifiedClientState]] = ...,
        clients_consensus : typing.Optional[typing.Iterable[ibc.core.client.v1.client_pb2.ClientConsensusStates]] = ...,
        clients_metadata : typing.Optional[typing.Iterable[global___IdentifiedGenesisMetadata]] = ...,
        params : typing.Optional[ibc.core.client.v1.client_pb2.Params] = ...,
        create_localhost : builtins.bool = ...,
        next_client_sequence : builtins.int = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"clients",b"clients",u"clients_consensus",b"clients_consensus",u"clients_metadata",b"clients_metadata",u"create_localhost",b"create_localhost",u"next_client_sequence",b"next_client_sequence",u"params",b"params"]) -> None: ...
global___GenesisState = GenesisState

class GenesisMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: builtins.bytes = ...
    value: builtins.bytes = ...

    def __init__(self,
        *,
        key : builtins.bytes = ...,
        value : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key",u"value",b"value"]) -> None: ...
global___GenesisMetadata = GenesisMetadata

class IdentifiedGenesisMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CLIENT_ID_FIELD_NUMBER: builtins.int
    CLIENT_METADATA_FIELD_NUMBER: builtins.int
    client_id: typing.Text = ...

    @property
    def client_metadata(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GenesisMetadata]: ...

    def __init__(self,
        *,
        client_id : typing.Text = ...,
        client_metadata : typing.Optional[typing.Iterable[global___GenesisMetadata]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"client_id",b"client_id",u"client_metadata",b"client_metadata"]) -> None: ...
global___IdentifiedGenesisMetadata = IdentifiedGenesisMetadata
