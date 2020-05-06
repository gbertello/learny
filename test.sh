CWD=$(cd $(dirname $0) && pwd)

for dir in */ ; do
  echo "Testing ${dir%/}..."
  $CWD/$dir/test.sh -s $SYSTEM
  echo ""
done
