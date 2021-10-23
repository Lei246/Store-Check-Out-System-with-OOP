from ProductRegister import ProductRegister
import os
from datetime import datetime

os.getcwd()
os.chdir(r'C:\Users\LEI\Github\python-programming\StoreData-System')


def getInputBetween(startval: int,endval: int)->int:
    while True:
        try:
            val = int(input("Mata in:"))
            if val >= startval and val <= endval:
                return val
            print(f"Ogiltigt val, mellan {startval} och {endval}, tack")
        except ValueError:
            print("Ange ett tal tack!")

def showTime():
    print("KASSA")
    now = datetime.now()
    print(f"KVITTO  {now}")
    
def startNewReceipt():
    productReg = ProductRegister()
    productReg.readFromFile("products.txt")
    while True: 
        print("Kommandon:")
        print("<productid> <antal>")
        print("PAY")
        kommando = input("Kommando:")
        if kommando == "PAY":
            #skriva till en fil
            return
            break
        parts = kommando.split(" ")
        productId = parts[0]

        product = productReg.find(productId)
        if product == None:
            print("Finns ej")
        else:
            productReg.addProduct(parts[0], parts[1])
            print(f"Bra - adding to receipt: {productReg.getName(product)}")        
            showTime()
            productReg.readFromFile(os.path)
            productReg.showKvitto()



while True:
    print("KASSA")
    print("1. Ny kund")
    print("0. Avsluta")
    sel = getInputBetween(0,1)
    if sel == 0:
        break
    if sel == 1:
        startNewReceipt()