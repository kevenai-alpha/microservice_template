import grpc
import logging
from functools import wraps
from google.protobuf.empty_pb2 import Empty
from types import FunctionType

from grpc_registry.generic_service.service_pb2_grpc import (
    add_GenericServiceServicer_to_server,
    GenericServiceServicer,
)

def wrapper(method):
    @wraps(method)
    def wrapped(*args, **kwargs):
        logging.debug(f"** RPC {method.__name__}")
        self = args[0]
        context = args[2]
        if self.remove:
            self.remove()
        try:
            res = method(*args, **kwargs)
        except IndexError as e:
            logging.error(f"IndexError: {e}")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(str(e))
            return Empty()

        if self.commit:
            self.commit()
        logging.debug(f"** RPC {method.__name__} END")
        return res

    return wrapped

class GRPCServiceMeta(type):
    def __new__(cls, class_name, bases, class_dict):
        return cls.process_methods(bases, class_dict, class_name)

    @classmethod
    def process_methods(cls, bases, class_dict, class_name):
        new_class_dict = {
            "commit": lambda self: None,
            "rollback": lambda self: None,
            "remove": lambda self: None,
        }
        for attribute_name, attribute in class_dict.items():
            if (
                isinstance(attribute, FunctionType)
                and attribute_name[0].isupper()
            ):
                attribute = wrapper(attribute)
            new_class_dict[attribute_name] = attribute

        res_class = type.__new__(cls, class_name, bases, new_class_dict)
        return res_class

class GenericGRPCService(GenericServiceServicer, metaclass=GRPCServiceMeta):
    def __init__(self):
        self.commit = None
        self.rollback = None
        self.remove = None

    def commit(self):
        pass

    def rollback(self):
        pass

    def remove(self):
        pass

    def ExampleMethod(self, request, context):
        logging.info("gRPC request received: %s", request)
        proto = SomeProtoResponse(message="Response from gRPC")
        return proto