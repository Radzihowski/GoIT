from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://goitlearn:goitlearn@cluster1.vyvxf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1",
    server_api=ServerApi('1')
)
db = client.book

result = db.cats.find({})
for el in result:
    print(el)
