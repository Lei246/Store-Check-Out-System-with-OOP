from registerRow import RegisterRow
from product import Product

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

    def showKvitto(self):
        priceTotal = 0
        for i in self._listOfProducts:
            priceI = i.getCount() * (i.getPrice(i._productId))
            print(f"{i.getName(i._productId)} {i.getCount()}*{i.getPrice(i._productId)} = {priceI} ")
            priceTotal = priceTotal + priceI
        print(f"Total to pay: {priceTotal}")

    def readFromFile(self,path:str):
        # läs från fil och stoppa in i listan
        with open('products.txt') as f:
            for line in f:
                self._listId.append(line.split(";")[0])

    def saveToFile(self, path:str):
        pass
        # sparar alla i listan till fil