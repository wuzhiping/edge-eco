FROM golang:1.19.5

USER root

RUN apt-get update
RUN apt-get install -y curl

RUN curl -s https://raw.githubusercontent.com/dapr/cli/master/install/install.sh?v=1 --insecure | /bin/bash

#RUN dapr init --slim 

RUN apt-get install -y net-tools dnsutils

COPY dapr /dapr

RUN mkdir $GOPATH/src/api && cd $_
WORKDIR /go/src/api

RUN go env -w GO111MODULE=off

RUN go get github.com/pilu/fresh

RUN go get github.com/kardianos/govendor
RUN govendor init
#RUN govendor fetch github.com/gin-gonic/gin
RUN go get github.com/gin-gonic/gin

RUN dapr init --slim

ADD main.go  /go/src/api

ADD start.sh /go/src/api



#ENTRYPOINT ["/entrypoint.sh"]
CMD /bin/bash ./start.sh
