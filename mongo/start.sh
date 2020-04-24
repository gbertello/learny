#!/bin/bash -e

CWD=$(cd $(dirname $0) && pwd)
PARENT=$(dirname $CWD)

source $CWD/lib/common.sh
source $CWD/config.sh

if [ -z $SYSTEM ]
then
  SYSTEM="dev"
fi

if [ -z $TARGET_PORT ]
then
  TARGET_PORT=80
fi

if [ -z $TARGET_VOLUME ]
then
  TARGET_VOLUME="/mnt/disk"
fi

while getopts ":p:s:" option; do
  case "${option}" in
    p)
      PORT=${OPTARG}
      ;;
    s)
      SYSTEM=${OPTARG}
      ;;
  esac
done

NETWORK=$SYSTEM
IMAGE=${PARENT##*/}_${CWD##*/}_${SYSTEM}

if [ ! -z $VOLUME ]
then
  DATADIR=$VOLUME/$SYSTEM
fi

stop -i $IMAGE &> /dev/null || true

OPTIONS=""

if [ ! -z $ENV ]
then
  OPTIONS="$OPTIONS -e $ENV"
fi

if [ ! -z $PORT ]
then
  OPTIONS="$OPTIONS -p $PORT:$TARGET_PORT"
fi

if [ ! -z $VOLUME ]
then
  mkdir -p $DATADIR
  OPTIONS="$OPTIONS -v $DATADIR:$TARGET_VOLUME"
fi

start -i $IMAGE -s $SYSTEM -n $NETWORK $OPTIONS

until docker exec $IMAGE mongo &> /dev/null
do
  sleep 5
done