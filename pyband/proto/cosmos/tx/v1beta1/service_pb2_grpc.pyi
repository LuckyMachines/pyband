"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc

from .service_pb2 import *
# Service defines a gRPC service for interacting with transactions.
class ServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    # Simulate simulates executing a transaction for estimating gas usage.
    Simulate:grpc.UnaryUnaryMultiCallable[
        global___SimulateRequest,
        global___SimulateResponse] = ...

    # GetTx fetches a tx by hash.
    GetTx:grpc.UnaryUnaryMultiCallable[
        global___GetTxRequest,
        global___GetTxResponse] = ...

    # BroadcastTx broadcast transaction.
    BroadcastTx:grpc.UnaryUnaryMultiCallable[
        global___BroadcastTxRequest,
        global___BroadcastTxResponse] = ...

    # GetTxsEvent fetches txs by event.
    GetTxsEvent:grpc.UnaryUnaryMultiCallable[
        global___GetTxsEventRequest,
        global___GetTxsEventResponse] = ...


# Service defines a gRPC service for interacting with transactions.
class ServiceServicer(metaclass=abc.ABCMeta):
    # Simulate simulates executing a transaction for estimating gas usage.
    @abc.abstractmethod
    def Simulate(self,
        request: global___SimulateRequest,
        context: grpc.ServicerContext,
    ) -> global___SimulateResponse: ...

    # GetTx fetches a tx by hash.
    @abc.abstractmethod
    def GetTx(self,
        request: global___GetTxRequest,
        context: grpc.ServicerContext,
    ) -> global___GetTxResponse: ...

    # BroadcastTx broadcast transaction.
    @abc.abstractmethod
    def BroadcastTx(self,
        request: global___BroadcastTxRequest,
        context: grpc.ServicerContext,
    ) -> global___BroadcastTxResponse: ...

    # GetTxsEvent fetches txs by event.
    @abc.abstractmethod
    def GetTxsEvent(self,
        request: global___GetTxsEventRequest,
        context: grpc.ServicerContext,
    ) -> global___GetTxsEventResponse: ...


def add_ServiceServicer_to_server(servicer: ServiceServicer, server: grpc.Server) -> None: ...
