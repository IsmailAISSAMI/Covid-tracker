from pymongo import MongoClient
import json
from pprint import pprint

#Connexion 
try:
    client = MongoClient('localhost',27017)
    db = client.covid
    globalData =  db.globalData
    paysData =  db.paysData
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
    print("Import globalData successfully!")

    with open('paysData.json', 'rb') as f:
        if db['paysData']:
            db['paysData'].drop()
            print('collection paysData droped!')
        paysData.insert_many(json.load(f))
    print("Import paysData successfully!")
except:
    print("Error: import data to dbase")

def display_all(globalData):
    for result in globalData.find():
        pprint(result)
    
def display_infection(globalData):
    for result in globalData.find({}, {"Infection":1, "_id":0, "Date":1}) :
        pprint(result)

# The statistic of the previous month (last 31 days)
def display_MonthStatistic(globalData):
    firstDay = globalData.find_one({})
    for i in globalData.find({}).skip(30):
        lastDay= i

    print(">>> Month Statistic :")
    print("- Infection: ", firstDay['Infection']-lastDay['Infection'])
    print("- Deces:", firstDay['Deces']-lastDay['Deces'])
    print("- Guerisons:", firstDay['Guerisons']-lastDay['Guerisons'])
    print("- TauxInfection:", firstDay['TauxInfection']-lastDay['TauxInfection'])
    print("- TauxDeces:", firstDay['TauxDeces']-lastDay['TauxDeces'])
    print("- TauxGuerison:", firstDay['TauxGuerison']-lastDay['TauxGuerison'])
    
    
# Methods
#display_all(globalData)
#display_infection(globalData)
display_MonthStatistic(globalData)