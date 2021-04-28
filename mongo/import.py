#!/usr/bin/env python3
import os
import subprocess as sp
from config import CWD, IMAGE

db = "test_db"
collection = "collection"
filename = os.path.join(CWD, "data", f"{collection}_import")
target_filename = f"/tmp/{collection}_import"

sp.run(["docker", "exec", IMAGE, "mongo", db, "--eval", "db.dropDatabase()"], stdout=open(os.devnull, 'w'))

sp.run(["docker", "cp", filename, f"{IMAGE}:{target_filename}"])
sp.run(["docker", "exec", IMAGE, "mongoimport", "--db", db, "--collection", collection, "--file", target_filename])
sp.run(["docker", "exec", IMAGE, "rm", target_filename])
