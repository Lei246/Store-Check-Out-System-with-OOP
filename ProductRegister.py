from registerRow import RegisterRow
from product import Product
import os
from datetime import datetime


class ProductRegister:

    def __init__(self) :
        self._listOfProducts = []
        self._listId = []

    def find(self, productid) -> Product:  
        for product in self._listId:
            if product == productid:
                return product
        return None
    
    def getName(self, productId):
        with open('products.txt') as f:
            for line in f:
                if productId == line.split(";")[0]:
                    return line.split(";")[1]

    def addProduct(self, productId, count):
        self._listOfProducts.append(RegisterRow(productId, count))

    def Kvitto(self):
        priceTotal = 0
        currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        kvittoList = [f"*** KVITTO  {currentTime}"]
        for i in self._listOfProducts:
            priceI = i.getCount() * (i.getPrice(i._productId))
            kvittoList.append(f"{i.getName(i._productId)} {i.getCount()}*{i.getPrice(i._productId)} = {priceI} ")
            priceTotal = priceTotal + priceI
        kvittoList.append(f"       Total to pay: {priceTotal}")
        return kvittoList


    def readAllProductsIDFromFile(self,path):
        with open('products.txt') as f:
            for line in f:
                self._listId.append(line.split(";")[0])

    def saveToFile(self):
        with open(f"Receipt_{datetime.today().strftime('%Y%m%d')}.txt", 'a') as f:
            for element in self.Kvitto():
                f.write(element + " \n")
