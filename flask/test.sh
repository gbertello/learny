#!/bin/bash -e

CWD=$(cd $(dirname $0) && pwd)
PARENT=$(dirname $CWD)
DOCKERFILE=Dockerfile
ENV=local
IMAGE=${PARENT##*/}_${CWD##*/}_${ENV}

DOCKERFILE_TEST=${DOCKERFILE}_test
ENV_TEST=${ENV}_test
IMAGE_TEST=${IMAGE}_test

docker stop $IMAGE &> /dev/null || true
docker rm $IMAGE &> /dev/null || true
docker stop $IMAGE_TEST &> /dev/null || true
docker rm $IMAGE_TEST &> /dev/null || true

docker network create --driver bridge $ENV &> /dev/null || true
docker build -t $IMAGE -f $DOCKERFILE $CWD > /dev/null
docker run -dit -e ENV=$ENV --name $IMAGE --network=$ENV $IMAGE > /dev/null

docker build -t $IMAGE_TEST -f $DOCKERFILE_TEST $CWD > /dev/null
docker run -dit -e ENV=$ENV_TEST --name $IMAGE_TEST --network=$ENV $IMAGE_TEST > /dev/null

docker exec $IMAGE_TEST pytest -q --color=yes test.py

docker stop $IMAGE_TEST > /dev/null
docker rm $IMAGE_TEST > /dev/null

docker stop $IMAGE > /dev/null
docker rm $IMAGE > /dev/null