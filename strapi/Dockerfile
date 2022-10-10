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

RUN npm install -y pg

#RUN npm install strapi-plugin-entity-relationship-chart --save
RUN npm install @strapi/plugin-graphql --save
RUN npm install @strapi/plugin-documentation
#RUN npm install strapi-plugin-custom-api
#RUN npm install strapi-plugin-todo
#RUN npm install @webbio/strapi-plugin-scheduler
#RUN yarn add strapi-plugin-notes
#RUN yarn add @chartbrew/plugin-strapi
#RUN yarn add strapi-plugin-comments
#RUN yarn add @notum-cz/strapi-plugin-content-versioning
#RUN yarn add strapi-plugin-ezforms
#RUN yarn add @localazy/strapi-plugin
#RUN yarn add strapi-plugin-pfapi
#RUN yarn add strapi-plugin-ratings

COPY ./src/admin/app.js /opt/app/src/admin/app.js

RUN npm run build

ADD start.sh /opt/app
COPY dapr /dapr

CMD /bin/bash ./start.sh
