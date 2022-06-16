from connect import Connect #引入connection string
from pymongo import MongoClient, collection, cursor

connection = Connect.get_connection()

db = connection.databaseuse 


cursor = db.collectionuse.find({'temperature':28}) #找出collectionuse 集合內 temperature 為 28 的資料

for collectionuse in cursor:#印出符合條件的結果
    print(collectionuse)
