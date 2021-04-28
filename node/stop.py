#!/usr/bin/env python3
from config import IMAGE
import os
import subprocess as sp


sp.run(["docker", "stop", IMAGE], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
sp.run(["docker", "rm", IMAGE], stdout=open(os.devnull, 'w'), stderr=open(os.devnull, 'w'))
