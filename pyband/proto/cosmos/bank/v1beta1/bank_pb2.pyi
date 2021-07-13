"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Params(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SEND_ENABLED_FIELD_NUMBER: builtins.int
    DEFAULT_SEND_ENABLED_FIELD_NUMBER: builtins.int
    default_send_enabled: builtins.bool = ...

    @property
    def send_enabled(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SendEnabled]: ...

    def __init__(self,
        *,
        send_enabled : typing.Optional[typing.Iterable[global___SendEnabled]] = ...,
        default_send_enabled : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"default_send_enabled",b"default_send_enabled",u"send_enabled",b"send_enabled"]) -> None: ...
global___Params = Params

class SendEnabled(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DENOM_FIELD_NUMBER: builtins.int
    ENABLED_FIELD_NUMBER: builtins.int
    denom: typing.Text = ...
    enabled: builtins.bool = ...

    def __init__(self,
        *,
        denom : typing.Text = ...,
        enabled : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"denom",b"denom",u"enabled",b"enabled"]) -> None: ...
global___SendEnabled = SendEnabled

class Input(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ADDRESS_FIELD_NUMBER: builtins.int
    COINS_FIELD_NUMBER: builtins.int
    address: typing.Text = ...

    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...

    def __init__(self,
        *,
        address : typing.Text = ...,
        coins : typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"address",b"address",u"coins",b"coins"]) -> None: ...
global___Input = Input

class Output(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ADDRESS_FIELD_NUMBER: builtins.int
    COINS_FIELD_NUMBER: builtins.int
    address: typing.Text = ...

    @property
    def coins(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...

    def __init__(self,
        *,
        address : typing.Text = ...,
        coins : typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"address",b"address",u"coins",b"coins"]) -> None: ...
global___Output = Output

class Supply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TOTAL_FIELD_NUMBER: builtins.int

    @property
    def total(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...

    def __init__(self,
        *,
        total : typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"total",b"total"]) -> None: ...
global___Supply = Supply

class DenomUnit(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DENOM_FIELD_NUMBER: builtins.int
    EXPONENT_FIELD_NUMBER: builtins.int
    ALIASES_FIELD_NUMBER: builtins.int
    denom: typing.Text = ...
    exponent: builtins.int = ...

    @property
    def aliases(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...

    def __init__(self,
        *,
        denom : typing.Text = ...,
        exponent : builtins.int = ...,
        aliases : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"aliases",b"aliases",u"denom",b"denom",u"exponent",b"exponent"]) -> None: ...
global___DenomUnit = DenomUnit

class Metadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DESCRIPTION_FIELD_NUMBER: builtins.int
    DENOM_UNITS_FIELD_NUMBER: builtins.int
    BASE_FIELD_NUMBER: builtins.int
    DISPLAY_FIELD_NUMBER: builtins.int
    description: typing.Text = ...
    base: typing.Text = ...
    display: typing.Text = ...

    @property
    def denom_units(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DenomUnit]: ...

    def __init__(self,
        *,
        description : typing.Text = ...,
        denom_units : typing.Optional[typing.Iterable[global___DenomUnit]] = ...,
        base : typing.Text = ...,
        display : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"base",b"base",u"denom_units",b"denom_units",u"description",b"description",u"display",b"display"]) -> None: ...
global___Metadata = Metadata
