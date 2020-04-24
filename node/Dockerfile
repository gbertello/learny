FROM node:8.15.1

RUN npm install --save \
  express@4.16.4

WORKDIR /app
COPY app/ .
CMD node app.js