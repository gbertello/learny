import subprocess


def run_file():
    return subprocess.check_output(["bash", "run.sh"]).decode("utf-8").strip()

def test_main():
    assert run_file() == "Hello, World!"

