import os
import subprocess

path = os.path.dirname(__file__)
    
def run_file(parameters):
    return subprocess.check_output(["bash", os.path.join(path, "..", "run.sh")] + parameters, cwd='.').decode("utf-8").strip()

def test_help():
    assert run_file(["-h"]).startswith("Usage")

def test_count_files():
    assert run_file(["-v", os.path.join(path, "disk")]) == "There are 2 file(s)"
