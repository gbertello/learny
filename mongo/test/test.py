from pymongo import MongoClient


def test_main():
  client = MongoClient("mongodb://learny_mongo_test:27017")
  db = client.test_database
  collection = db.test_collection
  collection.insert_one({"input": "Hello"})

  assert collection.count_documents({}) == 1
  
  client.drop_database("test_database")