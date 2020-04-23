import os
import subprocess


def run_file():
    path = os.path.dirname(__file__)
    return subprocess.check_output(["bash", os.path.join(path, "..", "run.sh")]).decode("utf-8").strip()

def test_main():
    assert run_file() == "Hello, World!"

