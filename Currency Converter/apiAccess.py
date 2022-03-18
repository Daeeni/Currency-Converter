import json
import requests

def getAccessKey():
    try:
        with open("accessKey.cfg") as f:
            line=f.readline()
            return line
    except FileNotFoundError:
        print("'accessKey.cfg' not found in current directory")
        return "Invalid-API-Key"

def getJsonCurrenciesShort():
    try:
        with open('currencies.json') as f:
            data = json.load(f)
            return data["currenciesShort"]
    except FileNotFoundError:
        print("'currencies.json' missing")
        return

def getJsonCurrenciesFull():
    try:
        with open('currencies.json') as f:
            data = json.load(f)
            return data["currencies"]
    except FileNotFoundError:
        print("'currencies.json' missing")
        return

def printCurrencies(currenciesDict):
    print("Possible currencies:")
    for key in currenciesDict:
        print(key+" = "+currenciesDict[key])
    print()

def getAllKeys():
    data = getJsonCurrenciesFull()
    allKeys = ""
    for key in data:
        allKeys += key+","
    return allKeys[:-1]

def getDatabaseList(fromP : str):
    access = "http://api.currencylayer.com/live?access_key="+getAccessKey()+"&source="+fromP+"&currencies="+getAllKeys()
    return access

def getJsonResponse(requestStr : str):
    req = requests.get(requestStr, verify = False)
    return req.json()

def getJsonResponseList(fromP : str):
    return getJsonResponse(getDatabaseList(fromP))
