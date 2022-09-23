const DAPR = require("@dapr/dapr");
const request = require("request");

const http = new DAPR.DaprClient("localhost", "3500");
module.exports = {
    daprClient : http,
    DaprClient : DAPR.DaprClient,
    HttpMethod : DAPR.HttpMethod,
    CommunicationProtocolEnum : DAPR.CommunicationProtocolEnum,
      LogLevel : DAPR.LogLevel,

        invoke : function(node,api,method,payload,headers,cb){
                     request( {
                                  url: "http:\/\/"+http.daprHost+":"+http.daprPort+"/v1.0/invoke/"+node+"/method"+api,
                               method: method || "GET",
                              headers: headers || { 'Content-Type': 'application/json' },
                                 json: payload || { }
                               }, cb);
                 }
};
