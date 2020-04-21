docker build -t ${PWD##*/} . > /dev/null
docker run ${PWD##*/}

