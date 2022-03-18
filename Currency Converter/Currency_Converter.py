from tkinter import *
from apiAccess import *
from dataAccess import *

def calculateSpecific():
    print("Enter Currency.")
    fromCur = input()
    print("Calculate to?")
    toCur = input()
    print("Enter Amount.")
    amount = input()
    printJsonConvert(fromCur, toCur, amount)

def calculateListShort():
    printCurrencies(getJsonCurrenciesShort())
    print("Enter Currency.")
    fromCur = input()
    print("Enter Amount.")
    amount = input()
    printJsonListShort(fromCur, amount)

def calculateList():
    printCurrencies(getJsonCurrenciesFull())
    print("Enter Currency.")
    fromCur = input()
    print("Enter Amount.")
    amount = input()
    printJsonListAll(fromCur, amount)

def main():
    print("Press 1 to specify a currency and amount to get all possible currency conversions"+
        "\nPress 2 to specify a currency and amount to get the most common currency conversions"+
        "\nPress 3 to specify a currency and amount to convert to a specific other currency")
    desicion=input()
    if(desicion == "1"):
        calculateList()
    elif(desicion=="2"):
        calculateListShort()
    elif(desicion=="3"):
        calculateSpecific()
    else:
        print("invalid input")
        main()

if __name__ == "__main__":
    main()