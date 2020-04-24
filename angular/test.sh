#!/bin/bash -e

CWD=$(cd $(dirname $0) && pwd)
PARENT=$(dirname $CWD)

source $CWD/lib/common.sh

SYSTEM="test"

NETWORK=$SYSTEM
IMAGE=${PARENT##*/}_${CWD##*/}_${SYSTEM}

if [ ! -z $VOLUME ]
then
  DATADIR=$VOLUME/$SYSTEM
fi

SYSTEM_TEST="pytest"

DOCKERFILE_TEST=$CWD/Dockerfile_test
IMAGE_TEST=${PARENT##*/}_${CWD##*/}_${SYSTEM_TEST}

stop -i $IMAGE_TEST &> /dev/null || true
stop -i $IMAGE &> /dev/null || true

if [ ! -z $VOLUME ]
then
  rm -rf $DATADIR
fi

OPTIONS=""

if [ ! -z $ENV ]
then
  OPTIONS="$OPTIONS -e $ENV"
fi

if [ ! -z $VOLUME ]
then
  mkdir -p $DATADIR
  OPTIONS="$OPTIONS -v $DATADIR:$TARGET_VOLUME"
fi

start -i $IMAGE -n $NETWORK -s $SYSTEM $OPTIONS
start -i $IMAGE_TEST -d $DOCKERFILE_TEST -n $NETWORK -s $SYSTEM_TEST

docker exec $IMAGE_TEST pytest -q --color=yes test.py

stop -i $IMAGE_TEST &> /dev/null || true
stop -i $IMAGE &> /dev/null || true

if [ ! -z $VOLUME ]
then
  rm -rf $DATADIR
fi