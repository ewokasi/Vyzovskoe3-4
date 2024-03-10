from pymongo import MongoClient
import random
from bson.objectid import ObjectId

from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
collection = client['laba1_bd']['item']
alleya = client['laba1_bd']['alleya']
fountain = client['laba1_bd']['item']
statue = client['laba1_bd']['item']
kinds = ['Клен','Сосна','Береза','Дуб','Липа', 'Ель','Яблоня','Ива','Тополь','Пихта']


def insert_trees(count):
    for i in range(count):
        r_kind = random.randint(0,len(kinds)-1)
        r_year = random.randint(1990,2023)
        r_month = random.randint(1,11)
        r_day = random.randint(1,25)
        id = collection.insert_one({'kind':kinds[r_kind], 'plant': datetime(r_year, r_month, r_day), 'cut': datetime(r_year, r_month+1, r_day), "status": "tree"}).inserted_id
        if i%6==0:
            alleya.update_one(
                                {"_id" : ObjectId("65c9f3d77af9b337b832d3d2")},
                                 { "$push": { "items": {"id": id, "status":"tree"} } })
        elif i%6==1:
            alleya.update_one(
                                {"_id" : ObjectId("65d481a290dbdccbe343c183")},
                                 { "$push": { "items": {"id": id, "status":"tree"} } })
            
        elif i%6==2:
            alleya.update_one(
                                {"_id" : ObjectId("65d481d790dbdccbe343c184")},
                                 { "$push": { "items": {"id": id, "status":"tree"} } })
        elif i%6==3:
            alleya.update_one(
                                {"_id" : ObjectId("65d481e190dbdccbe343c185")},
                                 { "$push": { "items": {"id": id, "status":"tree"} } })
        elif i%6==4:
            alleya.update_one(
                                {"_id" : ObjectId("65d481ec90dbdccbe343c186")},
                                 { "$push": { "items": {"id": id, "status":"tree"} } })
        elif i%6==5:
            alleya.update_one(
                                {"_id" : ObjectId("65d4820890dbdccbe343c187")},
                                 { "$push": { "items": {"id": id, "status":"tree"} } })
    
        

def insert_fountains(count):
     for i in range(count):
        r_kind = random.randint(0,len(kinds)-1)
        r_year = random.randint(1990,2023)
        r_month = random.randint(1,11)
        r_day = random.randint(1,25)
        id = fountain.insert_one({'date': datetime(r_year, r_month, r_day), "status": "fountain"}).inserted_id
        if i%3==0:
            alleya.update_one(
                                {"_id" : ObjectId("65c9f3d77af9b337b832d3d2")},
                                { "$push": { "items": {"id": id, "status":"fountain"} } })
        elif i%3==1:
            alleya.update_one(
                                {"_id" : ObjectId("65d4820890dbdccbe343c187")},
                                { "$push": { "items": {"id": id, "status":"fountain"} } })
            
        elif i%3==2:
            alleya.update_one(
                                {"_id" : ObjectId("65d481ec90dbdccbe343c186")},
                                 { "$push": { "items": {"id": id, "status":"fountain"} } })
        


def insert_statue(count):
     for i in range(count):
        r_kind = random.randint(0,len(kinds)-1)
        r_year = random.randint(1990,2023)
        r_month = random.randint(1,11)
        r_day = random.randint(1,25)
        id = statue.insert_one({'date': datetime(r_year, r_month, r_day), "status":"statue"}).inserted_id
      
        if i%2==0:
            alleya.update_one(
                                {"_id" : ObjectId("65c9f3d77af9b337b832d3d2")},
                                 { "$push": { "items": {"id": id, "status":"statue"} } })
        
        elif i%2==1:
            alleya.update_one(
                                {"_id" : ObjectId("65d481ec90dbdccbe343c186")},
                                 { "$push": { "items": {"id": id, "status":"statue"} } })
    
if __name__=="__main__":
   insert_fountains(2)
   insert_trees(10)
   insert_statue(4)