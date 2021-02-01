from pymongo import MongoClient
import json
from pprint import pprint

#Connexion 
try:
    client = MongoClient('localhost',27017)
    db = client.covid
    globalData =  db.globalData
    print("connection success")
except:
    print("error!")

# Import JSON
try: 
    with open('globalData.json', 'rb') as f:
        globalData.insert_many(json.load(f))
    print("import success!")
except:
    print("Error: import data to dbase")

def display_all(globalData):
    for result in globalData.find():
        pprint(result)
    

    
# Methods
display_all(globalData)
