from connect import Connect
from pymongo import MongoClient, collection, cursor


connection = Connect.get_connection()

db = connection.databaseuse

db.collectionuse.update_many(
    {"temperature":28},#把所有符合該條件的資料
    { "$set" : {"Humidity" : 80}}#更改為"Humidity" : 80
)


cursor = db.collectionuse.find({})

for collectionuse in cursor:
    print(collectionuse)