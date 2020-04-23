#!/bin/bash -e

CWD=$(cd $(dirname $0) && pwd)
PARENT=$(dirname $CWD)
DOCKERFILE=Dockerfile

ENV=staging
while getopts ":e:" option; do
  case "${option}" in
    e)
      ENV=${OPTARG}
      ;;
  esac
done

IMAGE=${PARENT##*/}_${CWD##*/}_${ENV}

docker network create --driver bridge $ENV &> /dev/null || true
docker build -t $IMAGE -f $DOCKERFILE $CWD > /dev/null
docker run -dit -e ENV=$ENV --name $IMAGE --network=$ENV $IMAGE > /dev/null