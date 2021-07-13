"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import cosmos.bank.v1beta1.bank_pb2
import cosmos.base.query.v1beta1.pagination_pb2
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class QueryBalanceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ADDRESS_FIELD_NUMBER: builtins.int
    DENOM_FIELD_NUMBER: builtins.int
    address: typing.Text = ...
    denom: typing.Text = ...

    def __init__(self,
        *,
        address : typing.Text = ...,
        denom : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"address",b"address",u"denom",b"denom"]) -> None: ...
global___QueryBalanceRequest = QueryBalanceRequest

class QueryBalanceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BALANCE_FIELD_NUMBER: builtins.int

    @property
    def balance(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...

    def __init__(self,
        *,
        balance : typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"balance",b"balance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"balance",b"balance"]) -> None: ...
global___QueryBalanceResponse = QueryBalanceResponse

class QueryAllBalancesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ADDRESS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int
    address: typing.Text = ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageRequest: ...

    def __init__(self,
        *,
        address : typing.Text = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageRequest] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"address",b"address",u"pagination",b"pagination"]) -> None: ...
global___QueryAllBalancesRequest = QueryAllBalancesRequest

class QueryAllBalancesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BALANCES_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def balances(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    def __init__(self,
        *,
        balances : typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"balances",b"balances",u"pagination",b"pagination"]) -> None: ...
global___QueryAllBalancesResponse = QueryAllBalancesResponse

class QueryTotalSupplyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___QueryTotalSupplyRequest = QueryTotalSupplyRequest

class QueryTotalSupplyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SUPPLY_FIELD_NUMBER: builtins.int

    @property
    def supply(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...

    def __init__(self,
        *,
        supply : typing.Optional[typing.Iterable[cosmos.base.v1beta1.coin_pb2.Coin]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"supply",b"supply"]) -> None: ...
global___QueryTotalSupplyResponse = QueryTotalSupplyResponse

class QuerySupplyOfRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DENOM_FIELD_NUMBER: builtins.int
    denom: typing.Text = ...

    def __init__(self,
        *,
        denom : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"denom",b"denom"]) -> None: ...
global___QuerySupplyOfRequest = QuerySupplyOfRequest

class QuerySupplyOfResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    AMOUNT_FIELD_NUMBER: builtins.int

    @property
    def amount(self) -> cosmos.base.v1beta1.coin_pb2.Coin: ...

    def __init__(self,
        *,
        amount : typing.Optional[cosmos.base.v1beta1.coin_pb2.Coin] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"amount",b"amount"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"amount",b"amount"]) -> None: ...
global___QuerySupplyOfResponse = QuerySupplyOfResponse

class QueryParamsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self,
        ) -> None: ...
global___QueryParamsRequest = QueryParamsRequest

class QueryParamsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARAMS_FIELD_NUMBER: builtins.int

    @property
    def params(self) -> cosmos.bank.v1beta1.bank_pb2.Params: ...

    def __init__(self,
        *,
        params : typing.Optional[cosmos.bank.v1beta1.bank_pb2.Params] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"params",b"params"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"params",b"params"]) -> None: ...
global___QueryParamsResponse = QueryParamsResponse

class QueryDenomsMetadataRequest(google.protobuf.message.Message):
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
global___QueryDenomsMetadataRequest = QueryDenomsMetadataRequest

class QueryDenomsMetadataResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    METADATAS_FIELD_NUMBER: builtins.int
    PAGINATION_FIELD_NUMBER: builtins.int

    @property
    def metadatas(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.bank.v1beta1.bank_pb2.Metadata]: ...

    @property
    def pagination(self) -> cosmos.base.query.v1beta1.pagination_pb2.PageResponse: ...

    def __init__(self,
        *,
        metadatas : typing.Optional[typing.Iterable[cosmos.bank.v1beta1.bank_pb2.Metadata]] = ...,
        pagination : typing.Optional[cosmos.base.query.v1beta1.pagination_pb2.PageResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"pagination",b"pagination"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"metadatas",b"metadatas",u"pagination",b"pagination"]) -> None: ...
global___QueryDenomsMetadataResponse = QueryDenomsMetadataResponse

class QueryDenomMetadataRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DENOM_FIELD_NUMBER: builtins.int
    denom: typing.Text = ...

    def __init__(self,
        *,
        denom : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"denom",b"denom"]) -> None: ...
global___QueryDenomMetadataRequest = QueryDenomMetadataRequest

class QueryDenomMetadataResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    METADATA_FIELD_NUMBER: builtins.int

    @property
    def metadata(self) -> cosmos.bank.v1beta1.bank_pb2.Metadata: ...

    def __init__(self,
        *,
        metadata : typing.Optional[cosmos.bank.v1beta1.bank_pb2.Metadata] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"metadata",b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"metadata",b"metadata"]) -> None: ...
global___QueryDenomMetadataResponse = QueryDenomMetadataResponse
