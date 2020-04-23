#!/bin/bash -e

CWD=$(cd $(dirname $0) && pwd)
PARENT=$(dirname $CWD)
VOLUME=$CWD/disk
DOCKERFILE=Dockerfile
ENV=local
IMAGE=${PARENT##*/}_${CWD##*/}_${ENV}

DOCKERFILE_TEST=${DOCKERFILE}_test
ENV_TEST=${ENV}_test
IMAGE_TEST=${IMAGE}_test

docker network create --driver bridge $ENV &> /dev/null || true
mkdir -p $VOLUME/$ENV
docker build -t $IMAGE -f $DOCKERFILE $CWD > /dev/null
docker run -dit -v $VOLUME/$ENV:/data/db -e ENV=$ENV --name $IMAGE --network=$ENV $IMAGE > /dev/null

until docker exec $IMAGE mongo &> /dev/null
do
  sleep 5
done

docker build -t $IMAGE_TEST -f $DOCKERFILE_TEST $CWD > /dev/null
docker run -dit -e ENV=$ENV_TEST --name $IMAGE_TEST --network=$ENV $IMAGE_TEST > /dev/null

docker exec $IMAGE_TEST pytest -q --color=yes test.py

docker stop $IMAGE_TEST > /dev/null
docker rm $IMAGE_TEST > /dev/null

docker stop $IMAGE > /dev/null
docker rm $IMAGE > /dev/null

rm -rf $VOLUME/$ENV