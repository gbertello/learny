### STAGE 1: Build ###
FROM node:12.7-alpine AS build
RUN npm install -g @angular/cli@9.1.8
WORKDIR /app
COPY app/package.json ./
RUN npm install
COPY app/ .
ARG ANGULAR_ENV
RUN ng build --configuration=$ANGULAR_ENV

### STAGE 2: Run ###
FROM nginx:1.17.1-alpine
COPY config/config.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist/app /usr/share/nginx/html/
