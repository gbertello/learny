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

IMAGE=${PARENT##*/}_${CWD##*/}_${SYSTEM}

stop -i $IMAGE
