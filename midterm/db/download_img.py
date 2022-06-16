from pymongo import MongoClient
from gridfs import *
import os
client=MongoClient('mongodb+srv://weiian:1234@cluster0.llxpm.mongodb.net/databaseTest1?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')
db=client.images

gridFS = GridFS(db, collection="fs")
count=0
for grid_out in gridFS.find({}):
    
    count+=1
    data = grid_out.read() # 獲取圖片資料
    outf = open("./images/image_{count}.jpg".format(count = count),'wb')#建立檔案並命名檔案名稱
    outf.write(data)  # 儲存圖片
    outf.close()