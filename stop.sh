CWD=$(cd $(dirname $0) && pwd)

SYSTEM="dev"
while getopts ":s:" option; do
  case "${option}" in
    s)
      SYSTEM=${OPTARG}
      ;;
  esac
done

echo "Stopping flask"
$CWD/flask/stop.sh -s $SYSTEM
echo ""

echo "Stopping mongo"
$CWD/mongo/stop.sh -s $SYSTEM
echo ""

echo "Stopping node"
$CWD/node/stop.sh -s $SYSTEM
echo ""

echo "Stopping angular"
$CWD/angular/stop.sh -s $SYSTEM
echo ""

echo "Stopping nginx"
$CWD/nginx/stop.sh -s $SYSTEM
echo ""
