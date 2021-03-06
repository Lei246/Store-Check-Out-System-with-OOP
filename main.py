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
    
def startNewReceipt():
    productReg = ProductRegister()
    productReg.readAllProductsIDFromFile("products.txt")
    while True: 
        print("KASSA")
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"KVITTO    {now}")
        print("Kommandon:")
        print("<productid> <antal>")
        print("PAY")
        kommando = input("Kommando:")
        if kommando == "PAY":
            print(productReg.saveToFile())
            break
        parts = kommando.split(" ")
        productId = parts[0]
        product = productReg.find(productId)
        if product == None:
            print("Finns ej")
        else:
            productReg.addProduct(parts[0], parts[1])
            print(*productReg.Kvitto(), sep="\n")


while True:
    print("KASSA")
    print("1. Ny kund")
    print("0. Avsluta")
    sel = getInputBetween(0,1)
    if sel == 0:
        break
    if sel == 1:
        startNewReceipt()