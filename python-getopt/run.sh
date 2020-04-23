CWD=$(cd `dirname $0` && pwd)
docker build -t ${CWD##*/} $CWD > /dev/null
docker run ${CWD##*/} python main.py $*