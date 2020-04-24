CWD=$(cd $(dirname $0) && pwd)

echo "Testing flask"
$CWD/flask/test.sh
echo ""

echo "Testing mongo"
$CWD/mongo/test.sh
echo ""

echo "Testing node"
$CWD/node/test.sh
echo ""

echo "Testing angular"
$CWD/angular/test.sh
echo ""