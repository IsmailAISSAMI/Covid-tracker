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
        if db['globalData']:
            db['globalData'].drop()
            print('collection globalData droped!')
        globalData.insert_many(json.load(f))
    print("import success!")
except:
    print("Error: import data to dbase")

def display_all(globalData):
    for result in globalData.find():
        pprint(result)
    
def display_infection(globalData):
    for result in globalData.find({}, {"Infection":1, "_id":0, "Date":1}) :
        pprint(result)

# total infections in the previous month
def display_infectionM(globalData):
    firstDay = globalData.find_one({}, {"Infection":1, "_id":0})
    for i in globalData.find({}, {"Infection":1, "_id":0}).skip(30):
        lastDay= i
    print("firstDay =",firstDay)
    print("lastDay =",lastDay)
    print("total infections in the previous month", firstDay['Infection']-lastDay['Infection'])
# Methods
#display_all(globalData)
#display_infection(globalData)
display_infectionM(globalData)