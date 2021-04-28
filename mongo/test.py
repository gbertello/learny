#!/usr/bin/env python3
from pymongo import MongoClient

def test_main():
  client = MongoClient("mongodb://localhost:3000", serverSelectionTimeoutMS=1)
  db = client.test_database
  collection = db.test_collection
  collection.insert_one({"input": "Hello"})

  assert collection.count_documents({}) == 1

  client.drop_database("test_database")

if __name__ == "__main__":
  import subprocess
  subprocess.run(["pytest", __file__])
