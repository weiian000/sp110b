from pymongo import MongoClient
from gridfs import * #匯入gridfs
import os #操作檔案要匯入os
#連結mongodb
client = MongoClient('mongodb+srv://weiian:1234@cluster0.llxpm.mongodb.net/databaseTest1?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')

db = client.images

dirs = 'C://test' #本地端照片存放路徑

files = os.listdir(dirs) #取得目錄下所有檔案

for file in files:
    filesname = dirs + '\\' +file 
    

    f = file.split('.') #以 . 作為分割檔名

    datatmp = open(filesname,'rb') #創建檔案

    imgput = GridFS(db)

    insertimg = imgput.put(datatmp,content_type=f[1],filename=f[0]) # 使用put將放入指定的資料庫 content_type=f[1]表示檔案類型.jpg filename=f[0]表示檔案名稱
    
    datatmp.close()