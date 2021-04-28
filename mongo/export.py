#!/usr/bin/env python3
import os
import subprocess as sp
from config import CWD, IMAGE

db = "test_db"
collection = "data"
filename = os.path.join(CWD, f"{collection}_export")
target_filename = f"/tmp/{collection}_export"


sp.run(["docker", "exec", IMAGE, "mongoexport", "--db", db, "--collection", collection, f"--out={target_filename}"])
sp.run(["docker", "cp", f"{IMAGE}:{target_filename}", filename])
sp.run(["docker", "exec", IMAGE, "rm", target_filename])
