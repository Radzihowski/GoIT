import json

from pymongo import MongoClient

client = MongoClient("mongodb://localhost")

client = MongoClient("mongodb://localhost")

db = client.hw

with open('quotes.json', 'r', emcoding='utf-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['author'],
            'tags': quote['tags']
        })