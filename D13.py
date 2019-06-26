"""
class Product:
    abdname = "fgh"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.abdname, self.age )

    def __del__(self):
        print("product deleted", self)

# p1 = Product()
p2 = Product("hi",21)

print(p2)
p2.show()

print(hex(id(p2)))
"""
# ======================----------/\/\\/\//\/\----------====================== #

class orders:

    def __init__(self, oid, price, restaurantName):
        self.oid = oid                                      # public
        self._price = price                                 # protected
        self.__restaurantName = restaurantName              # private

    def __showOrder(self):
        print(self.oid, self._price, self.__restaurantName)

o1 = orders(101, 3000, "anoi")
print(o1.__dict__)
print(orders.__dict__)


