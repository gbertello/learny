#!/usr/bin/env python3
import os
import subprocess as sp

CWD = os.path.dirname(os.path.abspath(__file__))
for dirname in os.listdir(CWD):
  script_name = os.path.join(dirname, "start.py")
  if os.path.exists(script_name):
    sp.run([script_name])
