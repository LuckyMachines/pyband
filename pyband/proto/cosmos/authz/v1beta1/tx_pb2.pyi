"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.authz.v1beta1.authz_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# MsgGrant is a request type for Grant method. It declares authorization to the grantee
# on behalf of the granter with the provided expiration time.
class MsgGrant(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GRANTER_FIELD_NUMBER: builtins.int
    GRANTEE_FIELD_NUMBER: builtins.int
    GRANT_FIELD_NUMBER: builtins.int
    granter: typing.Text = ...
    grantee: typing.Text = ...
    @property
    def grant(self) -> cosmos.authz.v1beta1.authz_pb2.Grant: ...
    def __init__(self,
        *,
        granter : typing.Text = ...,
        grantee : typing.Text = ...,
        grant : typing.Optional[cosmos.authz.v1beta1.authz_pb2.Grant] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"grant",b"grant"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"grant",b"grant",u"grantee",b"grantee",u"granter",b"granter"]) -> None: ...
global___MsgGrant = MsgGrant

# MsgExecResponse defines the Msg/MsgExecResponse response type.
class MsgExecResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULTS_FIELD_NUMBER: builtins.int
    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.bytes]: ...
    def __init__(self,
        *,
        results : typing.Optional[typing.Iterable[builtins.bytes]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"results",b"results"]) -> None: ...
global___MsgExecResponse = MsgExecResponse

# MsgExec attempts to execute the provided messages using
# authorizations granted to the grantee. Each message should have only
# one signer corresponding to the granter of the authorization.
class MsgExec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GRANTEE_FIELD_NUMBER: builtins.int
    MSGS_FIELD_NUMBER: builtins.int
    grantee: typing.Text = ...
    # Authorization Msg requests to execute. Each msg must implement Authorization interface
    # The x/authz will try to find a grant matching (msg.signers[0], grantee, MsgTypeURL(msg))
    # triple and validate it.
    @property
    def msgs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.any_pb2.Any]: ...
    def __init__(self,
        *,
        grantee : typing.Text = ...,
        msgs : typing.Optional[typing.Iterable[google.protobuf.any_pb2.Any]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"grantee",b"grantee",u"msgs",b"msgs"]) -> None: ...
global___MsgExec = MsgExec

# MsgGrantResponse defines the Msg/MsgGrant response type.
class MsgGrantResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MsgGrantResponse = MsgGrantResponse

# MsgRevoke revokes any authorization with the provided sdk.Msg type on the
# granter's account with that has been granted to the grantee.
class MsgRevoke(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GRANTER_FIELD_NUMBER: builtins.int
    GRANTEE_FIELD_NUMBER: builtins.int
    MSG_TYPE_URL_FIELD_NUMBER: builtins.int
    granter: typing.Text = ...
    grantee: typing.Text = ...
    msg_type_url: typing.Text = ...
    def __init__(self,
        *,
        granter : typing.Text = ...,
        grantee : typing.Text = ...,
        msg_type_url : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"grantee",b"grantee",u"granter",b"granter",u"msg_type_url",b"msg_type_url"]) -> None: ...
global___MsgRevoke = MsgRevoke

# MsgRevokeResponse defines the Msg/MsgRevokeResponse response type.
class MsgRevokeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___MsgRevokeResponse = MsgRevokeResponse
