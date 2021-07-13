"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.query.v1beta1.pagination_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import ibc.core.channel.v1.channel_pb2
import ibc.core.client.v1.client_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class QueryChannelRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PORT_ID_FIELD_NUMBER: builtins.int
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    port_id: typing.Text = ...
    channel_id: typing.Text = ...

    def __init__(self,
        *,
        port_id : typing.Text = ...,
        channel_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channel_id",b"channel_id",u"port_id",b"port_id"]) -> None: ...
global___QueryChannelRequest = QueryChannelRequest

class QueryChannelResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CHANNEL_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    proof: builtins.bytes = ...

    @property
    def channel(self) -> ibc.core.channel.v1.channel_pb2.Channel: ...

    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        channel : typing.Optional[ibc.core.channel.v1.channel_pb2.Channel] = ...,
        proof : builtins.bytes = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"channel",b"channel",u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channel",b"channel",u"proof",b"proof",u"proof_height",b"proof_height"]) -> None: ...
global___QueryChannelResponse = QueryChannelResponse

class QueryChannelsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> None: ...
global___QueryChannelsRequest = QueryChannelsRequest

class QueryChannelsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CHANNELS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int

    @property
    def channels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ibc.core.channel.v1.channel_pb2.IdentifiedChannel]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    @property
    def height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        channels : typing.Optional[typing.Iterable[ibc.core.channel.v1.channel_pb2.IdentifiedChannel]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"height",b"height",u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channels",b"channels",u"height",b"height",u"pagination",b"pagination"]) -> None: ...
global___QueryChannelsResponse = QueryChannelsResponse

class QueryConnectionChannelsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONNECTION_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    connection: typing.Text = ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        connection : typing.Text = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"connection",b"connection",u"pagination",b"pagination"]) -> None: ...
global___QueryConnectionChannelsRequest = QueryConnectionChannelsRequest

class QueryConnectionChannelsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CHANNELS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int

    @property
    def channels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ibc.core.channel.v1.channel_pb2.IdentifiedChannel]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    @property
    def height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        channels : typing.Optional[typing.Iterable[ibc.core.channel.v1.channel_pb2.IdentifiedChannel]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"height",b"height",u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channels",b"channels",u"height",b"height",u"pagination",b"pagination"]) -> None: ...
global___QueryConnectionChannelsResponse = QueryConnectionChannelsResponse

class QueryChannelClientStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PORT_ID_FIELD_NUMBER: builtins.int
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    port_id: typing.Text = ...
    channel_id: typing.Text = ...

    def __init__(self,
        *,
        port_id : typing.Text = ...,
        channel_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channel_id",b"channel_id",u"port_id",b"port_id"]) -> None: ...
global___QueryChannelClientStateRequest = QueryChannelClientStateRequest

class QueryChannelClientStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    IDENTIFIED_CLIENT_STATE_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    proof: builtins.bytes = ...

    @property
    def identified_client_state(self) -> ibc.core.client.v1.client_pb2.IdentifiedClientState: ...

    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        identified_client_state : typing.Optional[ibc.core.client.v1.client_pb2.IdentifiedClientState] = ...,
        proof : builtins.bytes = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"identified_client_state",b"identified_client_state",u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"identified_client_state",b"identified_client_state",u"proof",b"proof",u"proof_height",b"proof_height"]) -> None: ...
global___QueryChannelClientStateResponse = QueryChannelClientStateResponse

class QueryChannelConsensusStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PORT_ID_FIELD_NUMBER: builtins.int
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    REVISION_NUMBER_FIELD_NUMBER: builtins.int
    REVISION_HEIGHT_FIELD_NUMBER: builtins.int
    port_id: typing.Text = ...
    channel_id: typing.Text = ...
    revision_number: builtins.int = ...
    revision_height: builtins.int = ...

    def __init__(self,
        *,
        port_id : typing.Text = ...,
        channel_id : typing.Text = ...,
        revision_number : builtins.int = ...,
        revision_height : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channel_id",b"channel_id",u"port_id",b"port_id",u"revision_height",b"revision_height",u"revision_number",b"revision_number"]) -> None: ...
global___QueryChannelConsensusStateRequest = QueryChannelConsensusStateRequest

class QueryChannelConsensusStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONSENSUS_STATE_FIELD_NUMBER: builtins.int
    CLIENT_ID_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    client_id: typing.Text = ...
    proof: builtins.bytes = ...

    @property
    def consensus_state(self) -> google.protobuf.any_pb2.Any: ...

    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        consensus_state : typing.Optional[google.protobuf.any_pb2.Any] = ...,
        client_id : typing.Text = ...,
        proof : builtins.bytes = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"consensus_state",b"consensus_state",u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"client_id",b"client_id",u"consensus_state",b"consensus_state",u"proof",b"proof",u"proof_height",b"proof_height"]) -> None: ...
global___QueryChannelConsensusStateResponse = QueryChannelConsensusStateResponse

class QueryPacketCommitmentRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PORT_ID_FIELD_NUMBER: builtins.int
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    SEQUENCE_FIELD_NUMBER: builtins.int
    port_id: typing.Text = ...
    channel_id: typing.Text = ...
    sequence: builtins.int = ...

    def __init__(self,
        *,
        port_id : typing.Text = ...,
        channel_id : typing.Text = ...,
        sequence : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channel_id",b"channel_id",u"port_id",b"port_id",u"sequence",b"sequence"]) -> None: ...
global___QueryPacketCommitmentRequest = QueryPacketCommitmentRequest

class QueryPacketCommitmentResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COMMITMENT_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    commitment: builtins.bytes = ...
    proof: builtins.bytes = ...

    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        commitment : builtins.bytes = ...,
        proof : builtins.bytes = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"commitment",b"commitment",u"proof",b"proof",u"proof_height",b"proof_height"]) -> None: ...
global___QueryPacketCommitmentResponse = QueryPacketCommitmentResponse

class QueryPacketCommitmentsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PORT_ID_FIELD_NUMBER: builtins.int
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    port_id: typing.Text = ...
    channel_id: typing.Text = ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        port_id : typing.Text = ...,
        channel_id : typing.Text = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channel_id",b"channel_id",u"pagination",b"pagination",u"port_id",b"port_id"]) -> None: ...
global___QueryPacketCommitmentsRequest = QueryPacketCommitmentsRequest

class QueryPacketCommitmentsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COMMITMENTS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int

    @property
    def commitments(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ibc.core.channel.v1.channel_pb2.PacketState]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    @property
    def height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        commitments : typing.Optional[typing.Iterable[ibc.core.channel.v1.channel_pb2.PacketState]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"height",b"height",u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"commitments",b"commitments",u"height",b"height",u"pagination",b"pagination"]) -> None: ...
global___QueryPacketCommitmentsResponse = QueryPacketCommitmentsResponse

class QueryPacketReceiptRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PORT_ID_FIELD_NUMBER: builtins.int
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    SEQUENCE_FIELD_NUMBER: builtins.int
    port_id: typing.Text = ...
    channel_id: typing.Text = ...
    sequence: builtins.int = ...

    def __init__(self,
        *,
        port_id : typing.Text = ...,
        channel_id : typing.Text = ...,
        sequence : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channel_id",b"channel_id",u"port_id",b"port_id",u"sequence",b"sequence"]) -> None: ...
global___QueryPacketReceiptRequest = QueryPacketReceiptRequest

class QueryPacketReceiptResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RECEIVED_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    received: builtins.bool = ...
    proof: builtins.bytes = ...

    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        received : builtins.bool = ...,
        proof : builtins.bytes = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"proof",b"proof",u"proof_height",b"proof_height",u"received",b"received"]) -> None: ...
global___QueryPacketReceiptResponse = QueryPacketReceiptResponse

class QueryPacketAcknowledgementRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PORT_ID_FIELD_NUMBER: builtins.int
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    SEQUENCE_FIELD_NUMBER: builtins.int
    port_id: typing.Text = ...
    channel_id: typing.Text = ...
    sequence: builtins.int = ...

    def __init__(self,
        *,
        port_id : typing.Text = ...,
        channel_id : typing.Text = ...,
        sequence : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channel_id",b"channel_id",u"port_id",b"port_id",u"sequence",b"sequence"]) -> None: ...
global___QueryPacketAcknowledgementRequest = QueryPacketAcknowledgementRequest

class QueryPacketAcknowledgementResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ACKNOWLEDGEMENT_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    acknowledgement: builtins.bytes = ...
    proof: builtins.bytes = ...

    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        acknowledgement : builtins.bytes = ...,
        proof : builtins.bytes = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"acknowledgement",b"acknowledgement",u"proof",b"proof",u"proof_height",b"proof_height"]) -> None: ...
global___QueryPacketAcknowledgementResponse = QueryPacketAcknowledgementResponse

class QueryPacketAcknowledgementsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PORT_ID_FIELD_NUMBER: builtins.int
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    port_id: typing.Text = ...
    channel_id: typing.Text = ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        port_id : typing.Text = ...,
        channel_id : typing.Text = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channel_id",b"channel_id",u"pagination",b"pagination",u"port_id",b"port_id"]) -> None: ...
global___QueryPacketAcknowledgementsRequest = QueryPacketAcknowledgementsRequest

class QueryPacketAcknowledgementsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ACKNOWLEDGEMENTS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int

    @property
    def acknowledgements(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ibc.core.channel.v1.channel_pb2.PacketState]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    @property
    def height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        acknowledgements : typing.Optional[typing.Iterable[ibc.core.channel.v1.channel_pb2.PacketState]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"height",b"height",u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"acknowledgements",b"acknowledgements",u"height",b"height",u"pagination",b"pagination"]) -> None: ...
global___QueryPacketAcknowledgementsResponse = QueryPacketAcknowledgementsResponse

class QueryUnreceivedPacketsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PORT_ID_FIELD_NUMBER: builtins.int
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    PACKET_COMMITMENT_SEQUENCES_FIELD_NUMBER: builtins.int
    port_id: typing.Text = ...
    channel_id: typing.Text = ...

    @property
    def packet_commitment_sequences(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...

    def __init__(self,
        *,
        port_id : typing.Text = ...,
        channel_id : typing.Text = ...,
        packet_commitment_sequences : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channel_id",b"channel_id",u"packet_commitment_sequences",b"packet_commitment_sequences",u"port_id",b"port_id"]) -> None: ...
global___QueryUnreceivedPacketsRequest = QueryUnreceivedPacketsRequest

class QueryUnreceivedPacketsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SEQUENCES_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int

    @property
    def sequences(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...

    @property
    def height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        sequences : typing.Optional[typing.Iterable[builtins.int]] = ...,
        height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"height",b"height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"height",b"height",u"sequences",b"sequences"]) -> None: ...
global___QueryUnreceivedPacketsResponse = QueryUnreceivedPacketsResponse

class QueryUnreceivedAcksRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PORT_ID_FIELD_NUMBER: builtins.int
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    PACKET_ACK_SEQUENCES_FIELD_NUMBER: builtins.int
    port_id: typing.Text = ...
    channel_id: typing.Text = ...

    @property
    def packet_ack_sequences(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...

    def __init__(self,
        *,
        port_id : typing.Text = ...,
        channel_id : typing.Text = ...,
        packet_ack_sequences : typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channel_id",b"channel_id",u"packet_ack_sequences",b"packet_ack_sequences",u"port_id",b"port_id"]) -> None: ...
global___QueryUnreceivedAcksRequest = QueryUnreceivedAcksRequest

class QueryUnreceivedAcksResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SEQUENCES_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int

    @property
    def sequences(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...

    @property
    def height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        sequences : typing.Optional[typing.Iterable[builtins.int]] = ...,
        height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"height",b"height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"height",b"height",u"sequences",b"sequences"]) -> None: ...
global___QueryUnreceivedAcksResponse = QueryUnreceivedAcksResponse

class QueryNextSequenceReceiveRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PORT_ID_FIELD_NUMBER: builtins.int
    CHANNEL_ID_FIELD_NUMBER: builtins.int
    port_id: typing.Text = ...
    channel_id: typing.Text = ...

    def __init__(self,
        *,
        port_id : typing.Text = ...,
        channel_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channel_id",b"channel_id",u"port_id",b"port_id"]) -> None: ...
global___QueryNextSequenceReceiveRequest = QueryNextSequenceReceiveRequest

class QueryNextSequenceReceiveResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NEXT_SEQUENCE_RECEIVE_FIELD_NUMBER: builtins.int
    PROOF_FIELD_NUMBER: builtins.int
    PROOF_HEIGHT_FIELD_NUMBER: builtins.int
    next_sequence_receive: builtins.int = ...
    proof: builtins.bytes = ...

    @property
    def proof_height(self) -> ibc.core.client.v1.client_pb2.Height: ...

    def __init__(self,
        *,
        next_sequence_receive : builtins.int = ...,
        proof : builtins.bytes = ...,
        proof_height : typing.Optional[ibc.core.client.v1.client_pb2.Height] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"proof_height",b"proof_height"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"next_sequence_receive",b"next_sequence_receive",u"proof",b"proof",u"proof_height",b"proof_height"]) -> None: ...
global___QueryNextSequenceReceiveResponse = QueryNextSequenceReceiveResponse
