from pymongo import MongoClient
import random
from bson.objectid import ObjectId

from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
collection = client['laba1_bd']['tree']
alleya = client['laba1_bd']['alleya']
fountain = client['laba1_bd']['fountain']
statue = client['laba1_bd']['statue']
kinds = ['Клен','Сосна','Береза','Дуб','Липа', 'Ель','Яблоня','Ива','Тополь','Пихта']


def insert_trees(count):
    for i in range(count):
        r_kind = random.randint(0,len(kinds)-1)
        r_year = random.randint(1990,2023)
        r_month = random.randint(1,11)
        r_day = random.randint(1,25)
        id = collection.insert_one({'kind':kinds[r_kind], 'plant': datetime(r_year, r_month, r_day), 'cut': datetime(r_year, r_month+1, r_day)}).inserted_id
        if i%6==0:
            alleya.update_one(
                                {"_id" : ObjectId("65c9f3d77af9b337b832d3d2")},
                                { "$push": { "trees": id } })
        elif i%6==1:
            alleya.update_one(
                                {"_id" : ObjectId("65c9f3df7af9b337b832d3d3")},
                                { "$push": { "trees": id } })
            
        elif i%6==2:
            alleya.update_one(
                                {"_id" : ObjectId("65ca06897af9b337b832d3f5")},
                                { "$push": { "trees": id } })
        elif i%6==3:
            alleya.update_one(
                                {"_id" : ObjectId("65ca06917af9b337b832d3f6")},
                                { "$push": { "trees": id } })
        elif i%6==4:
            alleya.update_one(
                                {"_id" : ObjectId("65ca06997af9b337b832d3f7")},
                                { "$push": { "trees": id } })
        elif i%6==5:
            alleya.update_one(
                                {"_id" : ObjectId("65ca06aa7af9b337b832d3f8")},
                                { "$push": { "trees": id } })
    
        

def insert_fountains(count):
     for i in range(count):
        r_kind = random.randint(0,len(kinds)-1)
        r_year = random.randint(1990,2023)
        r_month = random.randint(1,11)
        r_day = random.randint(1,25)
        id = fountain.insert_one({'date': datetime(r_year, r_month, r_day)}).inserted_id
        if i%6==0:
            alleya.update_one(
                                {"_id" : ObjectId("65c9f3d77af9b337b832d3d2")},
                                { "$push": { "fountains": id } })
        elif i%6==1:
            alleya.update_one(
                                {"_id" : ObjectId("65c9f3df7af9b337b832d3d3")},
                                { "$push": { "fountains": id } })
            
        elif i%6==2:
            alleya.update_one(
                                {"_id" : ObjectId("65ca06897af9b337b832d3f5")},
                                { "$push": { "fountains": id } })
        elif i%6==3:
            alleya.update_one(
                                {"_id" : ObjectId("65ca06917af9b337b832d3f6")},
                                { "$push": { "fountains": id } })
    


def insert_statue(count):
     for i in range(count):
        r_kind = random.randint(0,len(kinds)-1)
        r_year = random.randint(1990,2023)
        r_month = random.randint(1,11)
        r_day = random.randint(1,25)
        id = statue.insert_one({'date': datetime(r_year, r_month, r_day)}).inserted_id
      
        if i%2==0:
            alleya.update_one(
                                {"_id" : ObjectId("65c9f3df7af9b337b832d3d3")},
                                { "$push": { "statue": id } })
            
        
        elif i%2==1:
            alleya.update_one(
                                {"_id" : ObjectId("65ca06917af9b337b832d3f6")},
                                { "$push": { "statue": id } })
    
#if __name__=="__main__":
#    insert_statue(3)