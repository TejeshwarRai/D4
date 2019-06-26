"""
class abc:
    # self is a reference var which will hold hashcode of current object
    # __init__ is constructor
    Schname = "fhjok"
    def __init__(self, name, phn, email):
        self.name = name
        self.phone = phn
        self.id = email

    def showDetails(self):
        print("name:", self.name)
        print("phone:", self.phone)
        print("email:", self.id)

s1 = abc("John", 9876543210, "kk@eh.in")
print("s1", s1)
s2 = abc("jkh", 8657998766, "eg@eg.eg")
print("s2", s2)
print(s1.__dict__)
print(s2.__dict__)

s1.psswrd = "gfd321"
print(s1.__dict__)

s1.showDetails()

print(s1.__dict__)
print(abc.__dict__)

"""



class Product:
    a = 0
    def __init__(self):
        Product.a += 1
    def showNumberOfObjects(self):
        print(Product.a)


p1 = Product()
p2 = Product()
p3 = Product()
p4 = p1
p5 = p3

p5.showNumberOfObjects()
