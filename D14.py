# class CA:
#     a = 10
#
#     def __init__(self):
#         self.b = 9
#
#     def show(self):
#         print(self.a)
#         print(self.b)
#         print(CA.a)
#         # print(CA.b)         # Property of object is not accessible by class
#         print(ca.a)
#         print(ca.b)
#
# ca = CA()
# ca.show()


# ============================================== #



class CA:
    a = 10

    def __init__(self):
        self.a = 9

    def show(self):
        print(self.a)
        print(CA.a)
        print(ca.a)


ca = CA()
ca.show()

