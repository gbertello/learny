CWD=$(cd $(dirname $0) && pwd)

for dir in $(find $CWD -mindepth 1 -maxdepth 1 -type d -not -path '*/\.*') ; do
  echo "Testing ${dir#./}..."
  $dir/test.sh -s $SYSTEM
done
