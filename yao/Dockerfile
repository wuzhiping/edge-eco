FROM ubuntu:20.04

ARG VERSION=0.10.1
ARG ARCH=amd64
RUN groupadd -r yao && useradd -r -g yao yao && \
    apt-get update && \
    apt-get install -y curl sudo procps net-tools dnsutils

RUN apt-get install -y vim
RUN apt-get install -y wget

RUN curl -s https://raw.githubusercontent.com/dapr/cli/master/install/install.sh | /bin/bash
#RUN wget -q https://raw.githubusercontent.com/dapr/cli/master/install/install.sh -O - | /bin/bash

RUN dapr -v

RUN dapr init --slim

RUN curl -fsSL "https://release-sv-1252011659.cos.na-siliconvalley.myqcloud.com/archives/yao-${VERSION}-linux-${ARCH}" > /usr/local/bin/yao && \
    chmod +x /usr/local/bin/yao

RUN mkdir -p /opt/app && \
    cd /opt/app && /usr/local/bin/yao init && \
    cd /opt/app && /usr/local/bin/yao migrate && \
    cd /opt/app && /usr/local/bin/yao run flows.setmenu && \
    sed -i 's/development/production/g' /opt/app/.env

RUN yao inspect
VOLUME /opt/app
WORKDIR /opt/app

COPY dapr /dapr

EXPOSE 5099

COPY start.sh /opt/app/
#CMD ["tail", "-f","/dev/null"]
#CMD ["/usr/local/bin/yao", "start"]
CMD /bin/bash ./start.sh
