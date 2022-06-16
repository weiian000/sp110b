from connect import Connect
from pymongo import MongoClient, collection, cursor
import matplotlib.pyplot as plt

connection = Connect.get_connection()

db = connection.hardware

#這邊用的是專題所使用的資料庫，先前看到的資料庫為另外創建的
cursor = db.tempmoist.find( {'tem':{'$ne': "0"}, "hum": {'$ne': 0} ,'soil': {'$ne':0},'time': {'$ne':0}})#找出欄位值不為0

hum = [] #創建空的陣列
tem = []
time = []
soil = []

for hardware in cursor: #利用迴圈將各欄位的值append到對應的陣列名稱
    tem1 = hardware["tem"]
    tem.append(tem1)
    hum1 = hardware["hum"]
    hum.append(hum1)
    time1 = hardware["time"]
    time.append(time1)
    soil1 = hardware["soil"]
    soil.append(soil1)

tem5 = tem[-5:] #使用python 陣列指定最後五筆資料

temf = list(map(int,tem5))#使用list以及map函數將原本的資料型態string轉為int

time5 = time[-5:]


plt.bar(time5,temf,width=0.2,color=['red'],label ="溫度")#溫度的最近五筆資料
plt.legend()
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"
plt.title("最近五筆記錄",fontsize=20)
plt.xlabel("時間",fontsize=15)
plt.ylabel("值")
for x,y in enumerate(temf):plt.text(x,y,'%s'%y,ha='center',fontsize=15)#將每一個長條圖的值顯示在圖表上
plt.show()
print('%s',time5)

soil5 = soil[-5:]
humf = list(map(float,soil5))#將土壤濕度的資料型態轉為float

plt.bar(time5,humf,width=0.2,color=['red'],label ="土壤濕度")#土壤濕度的最近五筆資料
plt.legend()
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"
plt.title("最近五筆記錄",fontsize=20)
plt.xlabel("時間",fontsize=15)
plt.ylabel("值")
for x,y in enumerate(humf):plt.text(x,y,'%s'%y,ha='center',fontsize=15)
plt.show()