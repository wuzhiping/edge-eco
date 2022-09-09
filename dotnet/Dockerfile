FROM  mcr.microsoft.com/dotnet/sdk:6.0 
WORKDIR /opt

USER root

RUN apt-get update
RUN apt-get install -y curl net-tools dnsutils

RUN curl -s https://raw.githubusercontent.com/dapr/cli/master/install/install.sh | /bin/bash

RUN dapr init --slim 

COPY dapr /dapr

WORKDIR /opt/app

RUN dotnet new webapi --no-https
RUN dotnet build

ADD start.sh /opt/app/start.sh
CMD /bin/bash ./start.sh
