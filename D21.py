# @ classmethod       # decorator
#
#
# @ staticmethod
# def greet(name):
#     print("Hello", name)
#

# =================================== #

# num = [2,3,4,5,6,7]
# lref = lambda num : num + num/10
#
# result = map(lref, num)
# print(result)
# print(list(result))
#
# l1 = [11,12,13,14,16,15,17]
# lref1 = lambda l1 : l1%2 ==0
# print(lref1)
# result1 = map(lref1,l1)
# print(result1)
# print(list(result1))
# result2 = filter(lref1,l1)
# print(result2)
# print(list(result2))

# ========================================= #
# num2 = [2,3,4,5,6,7]
# num1 = [5,3,2,6,7,1]
# lm2 = lambda p,q : p+q
# result3 = map(lm2, num2,num1)
# print(list(result3))

# ========================================= #

# lm4 = lambda p,q : p+q
# popu = [12345, 87976, 45676, 76876, 56567]
# from functools import reduce
# res = reduce(lm4, popu)
# print(res)
#


# ========================================= #

# def datagen():
#     file = open("D21point.txt", 'r')
#     lines = file.readlines()
#     for line in lines:
#         yield line
#
# dg = datagen()
# print(dg)
# print(next(dg))
# print(next(dg))
# print(next(dg))

# ========================================== #

