CWD=$(cd $(dirname $0) && pwd)

SYSTEM="dev"
while getopts ":s:" option; do
  case "${option}" in
    s)
      SYSTEM=${OPTARG}
      ;;
  esac
done

echo "Starting flask"
$CWD/flask/start.sh -s $SYSTEM
echo ""

echo "Starting mongo"
$CWD/mongo/start.sh -s $SYSTEM
echo ""

echo "Starting node"
$CWD/node/start.sh -s $SYSTEM
echo ""

echo "Starting angular"
$CWD/angular/start.sh -s $SYSTEM
echo ""

echo "Starting nginx"
$CWD/nginx/start.sh -s $SYSTEM
echo ""
