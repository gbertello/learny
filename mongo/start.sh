#!/bin/bash -e

CWD=$(cd $(dirname $0) && pwd)
PARENT=$(dirname $CWD)

source $CWD/lib/common.sh

SYSTEM=dev
VOLUME=$CWD/disk
TARGET_VOLUME="/data/db"

while getopts ":s:" option; do
  case "${option}" in
    s)
      SYSTEM=${OPTARG}
      ;;
  esac
done

NETWORK=$SYSTEM
IMAGE=${PARENT##*/}_${CWD##*/}_${SYSTEM}
DATADIR=$VOLUME/$SYSTEM

stop -i $IMAGE &> /dev/null || true

OPTIONS=""

if [[ $SYSTEM -eq "prod" ]]
then
  OPTIONS="$OPTIONS -r always"
fi

mkdir -p $DATADIR
OPTIONS="$OPTIONS -v $DATADIR:$TARGET_VOLUME"

start -i $IMAGE -s $SYSTEM -n $NETWORK $OPTIONS

until docker exec $IMAGE mongo &> /dev/null
do
  sleep 5
done
