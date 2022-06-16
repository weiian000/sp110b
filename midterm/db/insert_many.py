from connect import Connect
from pymongo import MongoClient, collection, cursor
import time

connection = Connect.get_connection()

db = connection.databaseuse
localtime = time.localtime()
result = time.strftime("%Y-%m-%d %I:%M:%S%p", localtime)

db.collectionuse.insert_many( [ #使用insert_many一次插入多筆資料 可以觀察time欄位時間為相同表示資料同時插入
    { "temperature" : 20, "Humidity" : 60, "time": result},
    { "temperature" : 24, "Humidity" : 55, "time": result},
    { "temperature" : 33, "Humidity" : 75, "time": result}
    ])

cursor = db.collectionuse.find({}) #find可以用來找出指定條件若無內容預設為全部內容

for collectionuse in cursor:
    print(collectionuse)    #印出資料庫內所有內容