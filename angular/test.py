#!/usr/bin/env python3
import requests
import subprocess


def test_main():
  r = requests.get("http://localhost:5001/").text.strip()
  assert r.startswith("<!doctype html>")

if __name__ == "__main__":
  subprocess.run(["pytest", __file__])
