#!/bin/bash -e

CWD=$(cd $(dirname $0) && pwd)
PARENT=$(dirname $CWD)
VOLUME=$CWD/disk
DOCKERFILE=Dockerfile
ENV=local

while getopts ":v:e:f:" option; do
  case "${option}" in
    v)
      VOLUME=${OPTARG}
      ;;
    e)
      ENV=${OPTARG}
      ;;
    f)
      DOCKERFILE=${OPTARG}
      ;;
  esac
done

IMAGE=${PARENT##*/}_${CWD##*/}_${ENV}

docker network create --driver bridge $ENV &> /dev/null || true
mkdir -p $VOLUME/$ENV
docker build -t $IMAGE -f $DOCKERFILE $CWD > /dev/null
docker run -dit -v $VOLUME/$ENV:/data/db -e ENV=$ENV --name $IMAGE --network=$ENV $IMAGE > /dev/null

until docker exec $IMAGE mongo &> /dev/null
do
  sleep 5
done