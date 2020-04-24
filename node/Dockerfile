FROM node:8.15.1

RUN npm install --save \
  express@4.16.4

COPY app /app
WORKDIR /app
CMD node app.js