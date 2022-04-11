# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from airavata_mft_sdk.ftp import FTPStorage_pb2 as ftp_dot_FTPStorage__pb2


class FTPStorageServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.listFTPStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.ftp.FTPStorageService/listFTPStorage',
                request_serializer=ftp_dot_FTPStorage__pb2.FTPStorageListRequest.SerializeToString,
                response_deserializer=ftp_dot_FTPStorage__pb2.FTPStorageListResponse.FromString,
                )
        self.getFTPStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.ftp.FTPStorageService/getFTPStorage',
                request_serializer=ftp_dot_FTPStorage__pb2.FTPStorageGetRequest.SerializeToString,
                response_deserializer=ftp_dot_FTPStorage__pb2.FTPStorage.FromString,
                )
        self.createFTPStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.ftp.FTPStorageService/createFTPStorage',
                request_serializer=ftp_dot_FTPStorage__pb2.FTPStorageCreateRequest.SerializeToString,
                response_deserializer=ftp_dot_FTPStorage__pb2.FTPStorage.FromString,
                )
        self.updateFTPStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.ftp.FTPStorageService/updateFTPStorage',
                request_serializer=ftp_dot_FTPStorage__pb2.FTPStorageUpdateRequest.SerializeToString,
                response_deserializer=ftp_dot_FTPStorage__pb2.FTPStorageUpdateResponse.FromString,
                )
        self.deleteFTPStorage = channel.unary_unary(
                '/org.apache.airavata.mft.resource.service.ftp.FTPStorageService/deleteFTPStorage',
                request_serializer=ftp_dot_FTPStorage__pb2.FTPStorageDeleteRequest.SerializeToString,
                response_deserializer=ftp_dot_FTPStorage__pb2.FTPStorageDeleteResponse.FromString,
                )


class FTPStorageServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def listFTPStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getFTPStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def createFTPStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateFTPStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteFTPStorage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FTPStorageServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'listFTPStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.listFTPStorage,
                    request_deserializer=ftp_dot_FTPStorage__pb2.FTPStorageListRequest.FromString,
                    response_serializer=ftp_dot_FTPStorage__pb2.FTPStorageListResponse.SerializeToString,
            ),
            'getFTPStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.getFTPStorage,
                    request_deserializer=ftp_dot_FTPStorage__pb2.FTPStorageGetRequest.FromString,
                    response_serializer=ftp_dot_FTPStorage__pb2.FTPStorage.SerializeToString,
            ),
            'createFTPStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.createFTPStorage,
                    request_deserializer=ftp_dot_FTPStorage__pb2.FTPStorageCreateRequest.FromString,
                    response_serializer=ftp_dot_FTPStorage__pb2.FTPStorage.SerializeToString,
            ),
            'updateFTPStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.updateFTPStorage,
                    request_deserializer=ftp_dot_FTPStorage__pb2.FTPStorageUpdateRequest.FromString,
                    response_serializer=ftp_dot_FTPStorage__pb2.FTPStorageUpdateResponse.SerializeToString,
            ),
            'deleteFTPStorage': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteFTPStorage,
                    request_deserializer=ftp_dot_FTPStorage__pb2.FTPStorageDeleteRequest.FromString,
                    response_serializer=ftp_dot_FTPStorage__pb2.FTPStorageDeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'org.apache.airavata.mft.resource.service.ftp.FTPStorageService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FTPStorageService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def listFTPStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.ftp.FTPStorageService/listFTPStorage',
            ftp_dot_FTPStorage__pb2.FTPStorageListRequest.SerializeToString,
            ftp_dot_FTPStorage__pb2.FTPStorageListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getFTPStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.ftp.FTPStorageService/getFTPStorage',
            ftp_dot_FTPStorage__pb2.FTPStorageGetRequest.SerializeToString,
            ftp_dot_FTPStorage__pb2.FTPStorage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def createFTPStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.ftp.FTPStorageService/createFTPStorage',
            ftp_dot_FTPStorage__pb2.FTPStorageCreateRequest.SerializeToString,
            ftp_dot_FTPStorage__pb2.FTPStorage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateFTPStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.ftp.FTPStorageService/updateFTPStorage',
            ftp_dot_FTPStorage__pb2.FTPStorageUpdateRequest.SerializeToString,
            ftp_dot_FTPStorage__pb2.FTPStorageUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteFTPStorage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/org.apache.airavata.mft.resource.service.ftp.FTPStorageService/deleteFTPStorage',
            ftp_dot_FTPStorage__pb2.FTPStorageDeleteRequest.SerializeToString,
            ftp_dot_FTPStorage__pb2.FTPStorageDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
