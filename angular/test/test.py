import requests


def test_main():
  r = requests.get("http://learny_angular_test:80/").text.strip()
  assert r.startswith("<!doctype html>")
