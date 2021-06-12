import pymongo 
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://pys_user:1234@cluster0.4p9k1.mongodb.net/Software_DB?retryWrites=true&w=majority")
db = cluster["Software_DB"]
collection = db["User"]

post = {"_id":"pinoa1228","pw": "1234", "name":"WoongSup"}

collection.insert_one(post)
