#!/bin/bash -e

CWD=$(cd $(dirname $0) && pwd)
PARENT=$(dirname $CWD)

source $CWD/lib/common.sh
TARGET_PORT=80

if [ -z $SYSTEM ]
then
  SYSTEM="dev"
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

if [[ $ENV -eq "prod" ]]
then
  OPTIONS="$OPTIONS -r always"
fi

start -i $IMAGE -s $SYSTEM -n $NETWORK $OPTIONS
