import os
import requests


def test_main():
  r = requests.get("http://learny_flask_test/").text.strip()
  assert r == "Hello World!"
  