start () {  
  local OPTIND # Needed for local getopts

  local DOCKERFILE=""
  local ENV=""
  local IMAGE=""
  local NETWORK=""
  local PORT=""
  local SYSTEM=""
  local VOLUME=""
  
  while getopts ":d:e:i:n:p:s:v:" option; do
    case "${option}" in
      d)
        DOCKERFILE=${OPTARG}
        ;;
      e)
        ENV=${OPTARG}
        ;;
      i)
        IMAGE=${OPTARG}
        ;;
      n)
        NETWORK=${OPTARG}
        ;;
      p)
        PORT=${OPTARG}
        ;;
      s)
        SYSTEM=${OPTARG}
        ;;
      v)
        VOLUME=${OPTARG}
        ;;
    esac
  done

  if [ ! -z $NETWORK ]
  then
    docker network create --driver bridge $NETWORK &> /dev/null || true
  fi

  local OPTIONS=""

  if [ ! -z $DOCKERFILE ]
  then
    OPTIONS="$OPTIONS -f $DOCKERFILE"
  fi
  
  docker build -t $IMAGE $OPTIONS $CWD > /dev/null

  OPTIONS=""
  
  for i in $(echo $ENV | tr ":" "\n")
  do
    OPTIONS="$OPTIONS -e $i"
  done
  
  if [ ! -z $IMAGE ]
  then
    OPTIONS="$OPTIONS --name $IMAGE"
  fi
  
  if [ ! -z $NETWORK ]
  then
    OPTIONS="$OPTIONS --network=$NETWORK"
  fi
  
  if [ ! -z $PORT ]
  then
    OPTIONS="$OPTIONS -p $PORT"
  fi
  
  if [ ! -z $VOLUME ]
  then
    OPTIONS="$OPTIONS -v $VOLUME"
  fi

  docker run -dit $OPTIONS $IMAGE > /dev/null
}

stop () {  
  local OPTIND # Needed for local getopts
  
  local IMAGE=""
  
  while getopts ":i:" option; do
    case "${option}" in
      i)
        IMAGE=${OPTARG}
        ;;
    esac
  done
 
  docker stop $IMAGE > /dev/null
  docker rm $IMAGE > /dev/null
}
