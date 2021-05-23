#!/usr/bin/env python3
import argparse
import os
import subprocess as sp
import time

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--system", default="dev", help="Specify system")
args = parser.parse_args()

CWD = os.path.dirname(os.path.abspath(__file__))
SYSTEM = args.system
NETWORK = SYSTEM
IMAGE = os.path.basename(os.path.dirname(CWD)) + "_" + os.path.basename(CWD) + "_" + SYSTEM
VOLUMES = {}
VARIABLES = {}
if SYSTEM == "dev":
  PORTS = {"5001": "80"}
else:
  PORTS = {}
RESTART = True if SYSTEM == "prod" else False

sp.run(["docker", "stop", IMAGE], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
sp.run(["docker", "rm", IMAGE], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))

if SYSTEM == "prod":
  sp.run(["docker", "build", "-t", IMAGE, "--build-arg", "ENV=production", CWD], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
else:
  sp.run(["docker", "build", "-t", IMAGE, "--build-arg", "ENV=" + SYSTEM, CWD], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))

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

sp.run(["docker", "ps"])
