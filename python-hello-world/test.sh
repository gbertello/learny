docker build -t ${PWD##*/}-test -f test/Dockerfile . > /dev/null
docker run -t -e "TERM=xterm-256color" ${PWD##*/}-test

