from pymongo import MongoClient
import random
from bson.objectid import ObjectId

from datetime import datetime
client = MongoClient("mongodb://localhost:27017/")
collection = client['laba1_bd']['tree']
alleya = client['laba1_bd']['alleya']


def test1():

    out = {'Ракетная Аллея': 0, 'Беговая Аллея': 0, 'Тройная липовая Аллея': 0, 'Театральная Аллея': 0}
    # Ищем аллеи, в названии которых встречается слово "клен"
    results = collection.find({"kind": {"$in": ["Клен"]}})
    for res in results:

        id=res['_id']
        all = alleya.find({"trees": {"$in": [ObjectId(id)]}})
        for a in all:
            out[a['name']]+=1

    print(out)

def test2():
  
    results = alleya.find( { '$where': "this.trees.length > 0 && this.fountains.length > 0" })
    for res in results:
        print(res["name"])

def test3():
    results = collection.find({}).sort({'plant':-1}).limit(1) 
    for res in results:
        print(res)

def test4():
    results = collection.aggregate([
    {
        "$group": {
        "_id": "$kind",
        "count": {
            "$sum": 1
        }
        }
    },
    {
        "$sort": {
        "count": -1
        }
    },
    {
        "$limit": 1
    }
    ])

    for res in results:
        print(res)

def test5():
    results = alleya.find( { '$where': "this.fountains.length ==0" })
    for res in results:
        print(res["name"])

test5()