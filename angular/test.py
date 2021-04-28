#!/usr/bin/env python3
import os
import requests

def test_main():
  r = requests.get("http://localhost:3000/").text.strip()
  assert r.startswith("<!doctype html>")

if __name__ == "__main__":
  import subprocess
  subprocess.run(["pytest", __file__])
