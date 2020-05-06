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
  echo "Stopping ${dir%/}..."
  $CWD/$dir/stop.sh -s $SYSTEM
done