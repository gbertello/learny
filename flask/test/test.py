import requests


def test_main():
  r = requests.get("http://learny_flask_local/").json()
  assert r == {"message": "Hello, World!"}
  