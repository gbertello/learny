import os
import subprocess

path = os.path.dirname(__file__)
    
def run_file(parameters):
    return subprocess.check_output(["bash", os.path.join(path, "..", "run.sh")] + parameters, cwd='.').decode("utf-8").strip()

def test_main_with_empty_string():
    assert run_file([]) == "Hello, Anonymous!"

def test_main_with_name():
    assert run_file(["Bob"]) == "Hello, Bob!"

def test_main_with_two_names():
    assert run_file(["Bob", "Alice"]) == "Hello, Bob Alice!"

def test_help():
    assert run_file(["-h"]).startswith("Usage")

def test_wrong_argument():
    process = subprocess.Popen(["bash", os.path.join(path, "..", "run.sh"), "-z"], cwd='.')
    process.communicate()
    assert process.returncode == 1