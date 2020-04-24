import requests


def test_main():
  r = requests.get("http://learny_node_test:80/").text.strip()
  assert r == "Hello World!"
  