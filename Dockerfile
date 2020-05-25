FROM node:12-alpine as base

WORKDIR /tmp/ui
COPY ui /tmp/ui
RUN npm i --production
RUN npm run build

FROM node:12-alpine

RUN mkdir -p ${APP_DIR}

# multi stage build
COPY --from=base /tmp/ui/dist ${APP_DIR}/public

WORKDIR ${APP_DIR}

COPY scenario-server/ ${APP_DIR}/

WORKDIR ${APP_DIR}
RUN npm i --production
CMD npm start
