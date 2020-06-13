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

stop -i $IMAGE &> /dev/null || true

OPTIONS=""
OPTIONS="$OPTIONS -e $ENV"

if [[ $SYSTEM -eq "prod" ]]
then
  OPTIONS="$OPTIONS -r always"
fi

start -i $IMAGE -s $SYSTEM -n $NETWORK $OPTIONS
