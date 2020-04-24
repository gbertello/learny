CWD=$(cd `dirname $0` && pwd)
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider $CWD/test/test.py