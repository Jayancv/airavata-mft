# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from airavata_mft_sdk.s3 import S3Credential_pb2 as s3_dot_S3Credential__pb2


class S3SecretServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getS3Secret = channel.unary_unary(
                '/org.apache.airavata.mft.credential.service.s3.S3SecretService/getS3Secret',
                request_serializer=s3_dot_S3Credential__pb2.S3SecretGetRequest.SerializeToString,
                response_deserializer=s3_dot_S3Credential__pb2.S3Secret.FromString,
                )
        self.createS3Secret = channel.unary_unary(
                '/org.apache.airavata.mft.credential.service.s3.S3SecretService/createS3Secret',
                request_serializer=s3_dot_S3Credential__pb2.S3SecretCreateRequest.SerializeToString,
                response_deserializer=s3_dot_S3Credential__pb2.S3Secret.FromString,
                )
        self.updateS3Secret = channel.unary_unary(
                '/org.apache.airavata.mft.credential.service.s3.S3SecretService/updateS3Secret',
                request_serializer=s3_dot_S3Credential__pb2.S3SecretUpdateRequest.SerializeToString,
                response_deserializer=s3_dot_S3Credential__pb2.S3SecretUpdateResponse.FromString,
                )
        self.deleteS3Secret = channel.unary_unary(
                '/org.apache.airavata.mft.credential.service.s3.S3SecretService/deleteS3Secret',
                request_serializer=s3_dot_S3Credential__pb2.S3SecretDeleteRequest.SerializeToString,
                response_deserializer=s3_dot_S3Credential__pb2.S3SecretDeleteResponse.FromString,
                )


class S3SecretServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getS3Secret(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createS3Secret(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateS3Secret(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteS3Secret(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_S3SecretServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getS3Secret': grpc.unary_unary_rpc_method_handler(
                    servicer.getS3Secret,
                    request_deserializer=s3_dot_S3Credential__pb2.S3SecretGetRequest.FromString,
                    response_serializer=s3_dot_S3Credential__pb2.S3Secret.SerializeToString,
            ),
            'createS3Secret': grpc.unary_unary_rpc_method_handler(
                    servicer.createS3Secret,
                    request_deserializer=s3_dot_S3Credential__pb2.S3SecretCreateRequest.FromString,
                    response_serializer=s3_dot_S3Credential__pb2.S3Secret.SerializeToString,
            ),
            'updateS3Secret': grpc.unary_unary_rpc_method_handler(
                    servicer.updateS3Secret,
                    request_deserializer=s3_dot_S3Credential__pb2.S3SecretUpdateRequest.FromString,
                    response_serializer=s3_dot_S3Credential__pb2.S3SecretUpdateResponse.SerializeToString,
            ),
            'deleteS3Secret': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteS3Secret,
                    request_deserializer=s3_dot_S3Credential__pb2.S3SecretDeleteRequest.FromString,
                    response_serializer=s3_dot_S3Credential__pb2.S3SecretDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'org.apache.airavata.mft.credential.service.s3.S3SecretService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class S3SecretService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getS3Secret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.credential.service.s3.S3SecretService/getS3Secret',
            s3_dot_S3Credential__pb2.S3SecretGetRequest.SerializeToString,
            s3_dot_S3Credential__pb2.S3Secret.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createS3Secret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.credential.service.s3.S3SecretService/createS3Secret',
            s3_dot_S3Credential__pb2.S3SecretCreateRequest.SerializeToString,
            s3_dot_S3Credential__pb2.S3Secret.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateS3Secret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.credential.service.s3.S3SecretService/updateS3Secret',
            s3_dot_S3Credential__pb2.S3SecretUpdateRequest.SerializeToString,
            s3_dot_S3Credential__pb2.S3SecretUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteS3Secret(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.credential.service.s3.S3SecretService/deleteS3Secret',
            s3_dot_S3Credential__pb2.S3SecretDeleteRequest.SerializeToString,
            s3_dot_S3Credential__pb2.S3SecretDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
