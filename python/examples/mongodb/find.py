from pymongo import MongoClient
import datetime

client = MongoClient()
db = client.demo

for p in db.people.find():
    print(p)

