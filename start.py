#!/usr/bin/env python3
from config import COMPONENTS
import os
import subprocess as sp

for component in COMPONENTS:
  sp.run([os.path.join(component, "start.py")])
