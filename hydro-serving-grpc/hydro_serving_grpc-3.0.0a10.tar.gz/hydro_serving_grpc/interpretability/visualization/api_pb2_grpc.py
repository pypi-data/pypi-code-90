# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from hydro_serving_grpc.interpretability.visualization import api_pb2 as hydro__serving__grpc_dot_interpretability_dot_visualization_dot_api__pb2


class VisualizationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Fit = channel.unary_unary(
                '/hydrosphere.interpretability.visualization.VisualizationService/Fit',
                request_serializer=hydro__serving__grpc_dot_interpretability_dot_visualization_dot_api__pb2.FitRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class VisualizationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Fit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VisualizationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Fit': grpc.unary_unary_rpc_method_handler(
                    servicer.Fit,
                    request_deserializer=hydro__serving__grpc_dot_interpretability_dot_visualization_dot_api__pb2.FitRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hydrosphere.interpretability.visualization.VisualizationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VisualizationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Fit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hydrosphere.interpretability.visualization.VisualizationService/Fit',
            hydro__serving__grpc_dot_interpretability_dot_visualization_dot_api__pb2.FitRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
