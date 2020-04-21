docker build -t ${PWD##*/}-test -f Dockerfile-test . > /dev/null
docker run -t -e "TERM=xterm-256color" ${PWD##*/}-test
