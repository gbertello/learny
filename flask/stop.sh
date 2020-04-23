#!/bin/bash -e

CWD=$(cd `dirname $0` && pwd)
PARENT=$(dirname $CWD)
ENV=staging

while getopts ":e:" option; do
  case "${option}" in
    e)
      ENV=${OPTARG}
      ;;
  esac
done

IMAGE=${PARENT##*/}_${CWD##*/}_$ENV

docker stop $IMAGE > /dev/null
docker rm $IMAGE > /dev/null