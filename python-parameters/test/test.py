import os
import subprocess


def run_file(parameters):
    path = os.path.dirname(__file__)
    return subprocess.check_output(["bash", os.path.join(path, "..", "run.sh")] + parameters, cwd='.').decode("utf-8").strip()

def test_main_with_empty_string():
    assert run_file([]) == "Hello, Anonymous!"

def test_main_with_name():
    assert run_file(["Bob"]) == "Hello, Bob!"

def test_main_with_two_names():
    assert run_file(["Bob", "Alice"]) == "Hello, Bob Alice!"
