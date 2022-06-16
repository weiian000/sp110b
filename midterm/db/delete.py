from connect import Connect
from pymongo import MongoClient, collection, cursor


connection = Connect.get_connection()

db = connection.databaseuse

db.collectionuse.delete_many(#使用delete_many 刪除所有符合條件的資料
    {"Humidity" : 80} #條件為"Humidity" : 80
)


cursor = db.collectionuse.find({})

for collectionuse in cursor:
    print(collectionuse)