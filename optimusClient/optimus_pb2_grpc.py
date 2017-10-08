# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import optimusClient.optimus_pb2 as optimus__pb2


class OptimusStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateJob = channel.unary_unary(
        '/Optimus/CreateJob',
        request_serializer=optimus__pb2.Job.SerializeToString,
        response_deserializer=optimus__pb2.Job.FromString,
        )
    self.CreateMultipleJobs = channel.unary_unary(
        '/Optimus/CreateMultipleJobs',
        request_serializer=optimus__pb2.ListOfJobs.SerializeToString,
        response_deserializer=optimus__pb2.ListOfJobs.FromString,
        )
    self.GetJob = channel.unary_unary(
        '/Optimus/GetJob',
        request_serializer=optimus__pb2.RequestWithId.SerializeToString,
        response_deserializer=optimus__pb2.Job.FromString,
        )
    self.ListJobs = channel.unary_unary(
        '/Optimus/ListJobs',
        request_serializer=optimus__pb2.ListJobsRequest.SerializeToString,
        response_deserializer=optimus__pb2.ListOfJobs.FromString,
        )
    self.ModifyJob = channel.unary_unary(
        '/Optimus/ModifyJob',
        request_serializer=optimus__pb2.Job.SerializeToString,
        response_deserializer=optimus__pb2.Job.FromString,
        )
    self.PullPendingJobs = channel.unary_unary(
        '/Optimus/PullPendingJobs',
        request_serializer=optimus__pb2.ListJobsRequest.SerializeToString,
        response_deserializer=optimus__pb2.ListOfJobs.FromString,
        )


class OptimusServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateMultipleJobs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListJobs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ModifyJob(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PullPendingJobs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_OptimusServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateJob': grpc.unary_unary_rpc_method_handler(
          servicer.CreateJob,
          request_deserializer=optimus__pb2.Job.FromString,
          response_serializer=optimus__pb2.Job.SerializeToString,
      ),
      'CreateMultipleJobs': grpc.unary_unary_rpc_method_handler(
          servicer.CreateMultipleJobs,
          request_deserializer=optimus__pb2.ListOfJobs.FromString,
          response_serializer=optimus__pb2.ListOfJobs.SerializeToString,
      ),
      'GetJob': grpc.unary_unary_rpc_method_handler(
          servicer.GetJob,
          request_deserializer=optimus__pb2.RequestWithId.FromString,
          response_serializer=optimus__pb2.Job.SerializeToString,
      ),
      'ListJobs': grpc.unary_unary_rpc_method_handler(
          servicer.ListJobs,
          request_deserializer=optimus__pb2.ListJobsRequest.FromString,
          response_serializer=optimus__pb2.ListOfJobs.SerializeToString,
      ),
      'ModifyJob': grpc.unary_unary_rpc_method_handler(
          servicer.ModifyJob,
          request_deserializer=optimus__pb2.Job.FromString,
          response_serializer=optimus__pb2.Job.SerializeToString,
      ),
      'PullPendingJobs': grpc.unary_unary_rpc_method_handler(
          servicer.PullPendingJobs,
          request_deserializer=optimus__pb2.ListJobsRequest.FromString,
          response_serializer=optimus__pb2.ListOfJobs.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Optimus', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
