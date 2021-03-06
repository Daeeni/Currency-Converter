import json
from datetime import datetime
from apiAccess import *

def getCurTimestamp():
    timestamp = datetime.timestamp(datetime.now())
    return int(timestamp)

def formatToLocalFile(newDataFromApi):
    if not newDataFromApi["success"]:
        print("Error retrieving data from API: \nError code:"+str(newDataFromApi["error"]["code"])+"\nInfo: "+newDataFromApi["error"]["info"] )
        return None
    now = getCurTimestamp()
    listData = { "timestamp": now, "currencies" : newDataFromApi["quotes"] } 
    with open('localData.json', 'w') as outfile:
        json.dump(listData, outfile, indent=4)
    return listData

def loadLocalFile():
    try:
        with open('localData.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        return formatToLocalFile(getJsonResponseList("USD"))
    if(getCurTimestamp() - data["timestamp"] > 172800):
        return formatToLocalFile(getJsonResponseList("USD"))
    else:
        return data

def printJsonConvert(fromC, toC, amount):
    localData = loadLocalFile()
    if localData is None:
        exit()
    fromValue = localData["currencies"].get("USD"+fromC)
    toValue = localData["currencies"].get("USD"+toC)
    toReturn = (toValue / fromValue) * float(amount)
    print(str(amount)+" "+fromC+" = "+str(toReturn)+" "+toC)

def printJsonListAll(fromC, amount):
    localData = loadLocalFile()
    if localData is None:
        exit()
    fromValue = localData["currencies"].get("USD"+fromC)
    print(str(format(float(amount), '.2f'))+"\t\t"+fromC+":")
    for i in localData["currencies"]:
        endAmount = (localData["currencies"][i] / fromValue) * float(amount)
        if(fromC != i[3:]):
            if(len(str(format(endAmount,'.2f'))) > 6):
                print(str(format(endAmount,'.2f')), "\t"+i[3:])
            else:
                print(str(format(endAmount,'.2f')), "\t\t"+i[3:])

def printJsonListShort(fromC, amount):
    localData = loadLocalFile()
    if localData is None:
        exit()
    localShort = getJsonCurrenciesShort()
    fromValue = localData["currencies"].get("USD"+fromC)
    print(str(format(float(amount), '.2f'))+"\t\t"+fromC+":")
    for i in localData["currencies"]:
        endAmount = (localData["currencies"][i] / fromValue) * float(amount)
        if((i[3:] in localShort) and not (fromC == i[3:])):
            if(len(str(format(endAmount,'.2f'))) > 6):
                print(str(format(endAmount,'.2f')), "\t"+i[3:])
            else:
                print(str(format(endAmount,'.2f')), "\t\t"+i[3:])