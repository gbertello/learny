import subprocess


def run_file(filename):
    return subprocess.check_output(["python", filename]).decode("utf-8").strip()

def test_main():
    assert run_file("/app/main.py") == "Hello, World!"

