from connect import Connect
from pymongo import MongoClient, collection, cursor


connection = Connect.get_connection()

db = connection.databaseuse

db.collectionuse.update_one( #使用update_one 更改資料內容
    {"Humidity" : 60}, #找出collectionuse 符合條件的 。 這邊是找出 Humidity 為 65 的那筆資料
    {"$set" : {"temperature" : 34}}, #並將該筆資料中temperature欄位更改為 34
)


cursor = db.collectionuse.find({}) 

for collectionuse in cursor: #印出所有結果觀查是否資料產生變化
    print(collectionuse)