#!/usr/bin/env python3
import argparse
import os
import subprocess as sp
import time


cwd = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--system", default="dev", help="Specify system")
args = parser.parse_args()

# ---------- PARSE SYSTEM FROM COMMAND LINE -------------- #
SYSTEM = args.system

# ---------- DEFINE NETWORK -------------- #
NETWORK = SYSTEM

# ---------- DEFINE IMAGE NAME -------------- #
IMAGE = os.path.basename(os.path.dirname(cwd)) + "_" + os.path.basename(cwd) + "_" + SYSTEM

# ---------- DEFINE VOLUME -------------- #
VOLUMES = {os.path.join(cwd, "disk", SYSTEM): "/data/db"}

# ---------- DEFINE ENVIRONMENT VARIABLES -------------- #
VARIABLES = {}

# ---------- DEFINE PORTS -------------- #
PORTS = {}

# ---------- DEFINE RESTART -------------- #
RESTART = True if SYSTEM == "prod" else False

# ---------- PREPARE OPTIONS FOR DOCKER RUN ------------#
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

# ---------- RUN COMMANDS -------------- #
sp.run(["docker", "stop", IMAGE], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
sp.run(["docker", "rm", IMAGE], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
sp.run(["docker", "build", "-t", IMAGE, cwd], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
sp.run(["docker", "network", "create", "--driver", "bridge", NETWORK], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
sp.run(["docker", "run", "-dit", "--name", IMAGE, f"--network={NETWORK}", "-e", f"IMAGE={IMAGE}", "-e", f"SYSTEM={SYSTEM}"] + OPTIONS + [IMAGE], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))

# ---------- WAIT UNTIL MONGO IS RUNNING -------------- #
while True:
  child = sp.Popen(["docker", "exec", IMAGE, "mongo"], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
  child.communicate()[0]
  if child.returncode == 0:
    break
  time.sleep(5)
