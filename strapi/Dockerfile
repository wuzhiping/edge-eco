FROM node:lts
WORKDIR /opt/

USER root

RUN apt-get update
RUN apt-get install -y curl net-tools dnsutils

RUN pwd
RUN curl -s https://raw.githubusercontent.com/dapr/cli/master/install/install.sh --insecure | /bin/bash
#RUN wget -q https://raw.githubusercontent.com/dapr/cli/master/install/install.sh -O - | /bin/bash
RUN dapr -v
RUN dapr init --slim 

RUN npx create-strapi-app app --quickstart --no-run
# COPY app /opt/app
WORKDIR /opt/app

ADD start.sh /opt/app
COPY dapr /dapr

CMD /bin/bash ./start.sh
