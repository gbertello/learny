#!/usr/bin/env python3
import os
import requests

def test_main():
  r = requests.get("http://localhost:3001/").text.strip()
  assert r == "Hello World!"

if __name__ == "__main__":
  import subprocess
  subprocess.run(["pytest", __file__])
