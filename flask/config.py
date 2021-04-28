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
VOLUMES = {}
VARIABLES = {}
PORTS = {"3000": "80"}
RESTART = True if SYSTEM == "prod" else False
