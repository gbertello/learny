CWD=$(cd `dirname $0` && pwd)

volume=$CWD/disk
while getopts ":v:" option; do
  case "${option}" in
    v)
      volume=${OPTARG}
      ;;
  esac
done

docker build -t ${CWD##*/} $CWD > /dev/null
docker run -v $volume:/mnt/disk ${CWD##*/} python main.py $*