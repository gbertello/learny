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

# ---------- DEFINE IMAGE NAME -------------- #
IMAGE = os.path.basename(os.path.dirname(cwd)) + "_" + os.path.basename(cwd) + "_" + SYSTEM

# ---------- RUN COMMANDS -------------- #
sp.run(["docker", "stop", IMAGE], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
sp.run(["docker", "rm", IMAGE], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
