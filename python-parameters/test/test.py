import subprocess


def run_file(parameters):
    return subprocess.check_output(["bash", "run.sh"] + parameters, cwd='.').decode("utf-8").strip()

def test_main_with_empty_string():
    assert run_file([]) == "Hello, Anonymous!"

def test_main_with_name():
    assert run_file(["Bob"]) == "Hello, Bob!"

def test_main_with_two_names():
    assert run_file(["Bob", "Alice"]) == "Hello, Bob Alice!"
