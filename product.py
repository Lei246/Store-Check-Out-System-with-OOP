from pristyp import PrisTyp


class Product:
    def __init__(self, productId : str, price : float, pristyp : PrisTyp, namn: str ):
        self._productId = productId
        self._price = price 
        self._pristyp = pristyp
        self._namn = namn

    def getNamn(self):
        return self._namn

    def getProductId(self):
        return self._productId  