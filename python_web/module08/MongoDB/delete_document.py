from bson.objectid import ObjectId

from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://goitlearn:goitlearn@cluster1.vyvxf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1",
    server_api=ServerApi('1')
)
db = client.book

db.cats.delete_one({"name": "barsik"})
result = db.cats.find_one({"name": "barsik"})
print(result)