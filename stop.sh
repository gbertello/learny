CWD=$(cd $(dirname $0) && pwd)

SYSTEM="dev"
while getopts ":s:" option; do
  case "${option}" in
    s)
      SYSTEM=${OPTARG}
      ;;
  esac
done

for dir in $(find $CWD -mindepth 1 -maxdepth 1 -type d -not -path '*/\.*') ; do
  echo "Stopping ${dir#./}..."
  $dir/stop.sh -s $SYSTEM
done