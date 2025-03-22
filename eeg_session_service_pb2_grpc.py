# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import eeg_session_service_pb2 as eeg__session__service__pb2


class EEGSessionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AnalyzeSession = channel.unary_unary(
                '/EEGSessionService/AnalyzeSession',
                request_serializer=eeg__session__service__pb2.SessionRequest.SerializeToString,
                response_deserializer=eeg__session__service__pb2.SessionResponse.FromString,
                )


class EEGSessionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AnalyzeSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EEGSessionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AnalyzeSession': grpc.unary_unary_rpc_method_handler(
                    servicer.AnalyzeSession,
                    request_deserializer=eeg__session__service__pb2.SessionRequest.FromString,
                    response_serializer=eeg__session__service__pb2.SessionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EEGSessionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EEGSessionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AnalyzeSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/EEGSessionService/AnalyzeSession',
            eeg__session__service__pb2.SessionRequest.SerializeToString,
            eeg__session__service__pb2.SessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
