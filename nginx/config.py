#!/usr/bin/env python3
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--system", default="dev", help="Specify system")
args = parser.parse_args()

CWD = os.path.dirname(os.path.abspath(__file__))
SYSTEM = args.system
NETWORK = SYSTEM
IMAGE = os.path.basename(os.path.dirname(CWD)) + "_" + os.path.basename(CWD) + "_" + SYSTEM
VOLUMES = {os.path.join(CWD, "app"): "/usr/share/nginx/html"}
VARIABLES = {}
if SYSTEM == "dev":
  PORTS = {"5501": "80"}
else:
  PORTS = {}
RESTART = True if SYSTEM == "prod" else False
