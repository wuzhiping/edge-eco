#FROM openjdk:8-jdk-oracle
#FROM arm64v8/openjdk:8-jdk-oracle
FROM arm32v7/openjdk:8
WORKDIR /opt/

USER root

RUN curl -s https://raw.githubusercontent.com/dapr/cli/master/install/install.sh | /bin/bash

RUN dapr init --slim

COPY dapr /dapr

ADD start.sh /opt
ADD springboot-demo.jar /opt/

CMD /bin/bash ./start.sh
