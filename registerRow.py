from pristyp import PrisTyp
from product import Product

class RegisterRow(Product):
    def __init__(self, productId, count:float ):
        super().__init__(productId, "", "", "")
        self._productId = productId
        self._count = count

    def getProductId(self):
        return self._productId
    def getCount(self) -> float:
        return float(self._count)
    def getName(self, productId):
        with open('products.txt') as f:
            for line in f:
                if self._productId == line.split(";")[0]:
                    return line.split(";")[1]
    def getPrice(self, productId)-> float:
        with open('products.txt') as f:
            for line in f:
                if self._productId == line.split(";")[0]:
                    return float(line.split(";")[2])