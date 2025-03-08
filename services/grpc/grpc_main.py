import grpc
from concurrent import futures
from grpc_registry.generic_service.service_pb2_grpc import (add_GenericServiceServicer_to_server)
from services.grpc.services import GenericGRPCService

def get_grpc_server():
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        server = grpc.server(executor)
        add_GenericServiceServicer_to_server(GenericGRPCService(), server)
    return server

