import subprocess


def run_file(parameter):
    return subprocess.check_output(["bash", "run.sh", parameter]).decode("utf-8").strip()

def test_main_with_empty_string():
    assert run_file("") == "Hello, Anonymous!"

def test_main_with_name():
    assert run_file("Bob") == "Hello, Bob!"
