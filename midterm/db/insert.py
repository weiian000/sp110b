from connect import Connect
from pymongo import MongoClient, collection, cursor
import time

connection = Connect.get_connection()

db = connection.databaseuse #創建一個名為databaseuse的database
localtime = time.localtime()
result = time.strftime("%Y-%m-%d %I:%M:%S%p", localtime)#加入當前時間

db.collectionuse.insert_one( #使用insert_one插入單一筆資料進入名為collectionuse的collection
    { "temperature" : 28,       
        "Humidity" : 70,        #欄位與值
        "time"     : result     
    })

cursor = db.collectionuse.find({}) #find可以用來找出指定條件若無內容預設為全部內容

for collectionuse in cursor:
    print(collectionuse)    #資料庫內所有內容
