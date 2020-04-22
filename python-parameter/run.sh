docker build -t ${PWD##*/} . > /dev/null
docker run ${PWD##*/} python /app/main.py $1
