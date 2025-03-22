// package: 
// file: eeg_session_service.proto

var eeg_session_service_pb = require("./eeg_session_service_pb");
var grpc = require("@improbable-eng/grpc-web").grpc;

var EEGSessionService = (function () {
  function EEGSessionService() {}
  EEGSessionService.serviceName = "EEGSessionService";
  return EEGSessionService;
}());

EEGSessionService.AnalyzeSession = {
  methodName: "AnalyzeSession",
  service: EEGSessionService,
  requestStream: false,
  responseStream: false,
  requestType: eeg_session_service_pb.SessionRequest,
  responseType: eeg_session_service_pb.SessionResponse
};

exports.EEGSessionService = EEGSessionService;

function EEGSessionServiceClient(serviceHost, options) {
  this.serviceHost = serviceHost;
  this.options = options || {};
}

EEGSessionServiceClient.prototype.analyzeSession = function analyzeSession(requestMessage, metadata, callback) {
  if (arguments.length === 2) {
    callback = arguments[1];
  }
  var client = grpc.unary(EEGSessionService.AnalyzeSession, {
    request: requestMessage,
    host: this.serviceHost,
    metadata: metadata,
    transport: this.options.transport,
    debug: this.options.debug,
    onEnd: function (response) {
      if (callback) {
        if (response.status !== grpc.Code.OK) {
          var err = new Error(response.statusMessage);
          err.code = response.status;
          err.metadata = response.trailers;
          callback(err, null);
        } else {
          callback(null, response.message);
        }
      }
    }
  });
  return {
    cancel: function () {
      callback = null;
      client.close();
    }
  };
};

exports.EEGSessionServiceClient = EEGSessionServiceClient;

