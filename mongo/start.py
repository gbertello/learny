#!/usr/bin/env python3
from config import CWD, SYSTEM, NETWORK, IMAGE, VOLUMES, VARIABLES, PORTS, RESTART
import os
import subprocess as sp
import time


sp.run(["docker", "stop", IMAGE], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
sp.run(["docker", "rm", IMAGE], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
sp.run(["docker", "build", "-t", IMAGE, CWD], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
sp.run(["docker", "network", "create", "--driver", "bridge", NETWORK], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))

OPTIONS = []

if RESTART:
  OPTIONS += ["--restart", "always"]

for k, v in VARIABLES.items():
  OPTIONS += ["-e", f"{k}={v}"]

for k, v in PORTS.items():
  OPTIONS += ["-p", f"{k}:{v}"]

for k, v in VOLUMES.items():
  if not os.path.exists(k):
    os.makedirs(k)
  OPTIONS += ["-v", f"{k}:{v}"]

sp.run(["docker", "run", "-dit", "--name", IMAGE, f"--network={NETWORK}", "-e", f"IMAGE={IMAGE}", "-e", f"SYSTEM={SYSTEM}"] + OPTIONS + [IMAGE], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))

while True:
  child = sp.Popen(["docker", "exec", IMAGE, "mongo"], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
  child.communicate()[0]
  if child.returncode == 0:
    break
  time.sleep(5)
