#!/usr/bin/env python3
from pymongo import MongoClient
import subprocess


def test_main():
  client = MongoClient("mongodb://localhost:3001/", serverSelectionTimeoutMS=1)
  db = client.test_database
  collection = db.test_collection
  collection.insert_one({"input": "Hello"})

  assert collection.count_documents({}) == 1

  client.drop_database("test_database")

if __name__ == "__main__":
  subprocess.run(["pytest", __file__])
