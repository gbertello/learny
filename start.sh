CWD=$(cd $(dirname $0) && pwd)

SYSTEM="dev"
while getopts ":s:" option; do
  case "${option}" in
    s)
      SYSTEM=${OPTARG}
      ;;
  esac
done

for dir in */ ; do
  echo "Starting ${dir%/}"
  $CWD/$dir/start.sh -s $SYSTEM
done
