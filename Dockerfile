FROM node:12-alpine

ENV APP_DIR=/opt/app

ENV LOG4J_CONFIG_FILE=config/log4js.json

RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}

COPY server/ ${APP_DIR}/
COPY ui/dist ${APP_DIR}/public/
RUN npm i
CMD npm start
