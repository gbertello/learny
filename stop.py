#!/usr/bin/env python3
import os
import sys
import subprocess as sp

CWD = os.path.dirname(os.path.abspath(__file__))
for dirname in os.listdir(CWD):
  script_name = os.path.join(os.path.join(CWD, dirname), "stop.py")
  if os.path.exists(script_name):
    sp.run([script_name] + sys.argv[1:])
