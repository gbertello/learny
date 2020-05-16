#!/bin/bash -e

CWD=$(cd $(dirname $0) && pwd)
PARENT=$(dirname $CWD)

source $CWD/lib/common.sh

SYSTEM="dev"
while getopts ":s:" option; do
  case "${option}" in
    s)
      SYSTEM=${OPTARG}
      ;;
  esac
done

NETWORK=$SYSTEM
IMAGE=${PARENT##*/}_${CWD##*/}_${SYSTEM}
VOLUME="$CWD/app"
TARGET_VOLUME="/usr/share/nginx/html"
PORT=3000
TARGET_PORT=80

mkdir -p $VOLUME
stop -i $IMAGE &> /dev/null || true

OPTIONS=""

if [[ $ENV -eq "prod" ]]
then
  OPTIONS="$OPTIONS -r always"
fi

OPTIONS="$OPTIONS -v $VOLUME:$TARGET_VOLUME:ro"
OPTIONS="$OPTIONS -p $PORT:$TARGET_PORT"

start -i $IMAGE -s $SYSTEM -n $NETWORK $OPTIONS
