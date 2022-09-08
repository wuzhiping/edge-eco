FROM node:lts
WORKDIR /opt/bpm

USER root

RUN apt-get update
RUN apt-get install -y curl

RUN curl -s https://raw.githubusercontent.com/dapr/cli/master/install/install.sh | /bin/bash

RUN dapr init --slim 


RUN npm install pm2 -g
ADD package.json /opt/bpm
RUN npm install --loglevel verbose

ADD start.sh /opt/bpm
ADD bpm.js /opt/bpm/bpm.js
Add openApi.js /opt/bpm/openApi.js

RUN npm install @dapr/dapr @supabase/postgrest-js

RUN apt-get install -y net-tools dnsutils
COPY dapr /dapr
COPY entrypoint.sh /entrypoint.sh
#ENTRYPOINT ["/entrypoint.sh"]
CMD /bin/bash ./start.sh
