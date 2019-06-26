import numpy as np
import pandas as pa
"""
a = [10, 20, 30, 40, 50]
print(a, type(a))

print()

b = np.array(a)
print(b, type(b))

# c = np.array([10, 20, 30, 40, 50])
# print(c, type(c))

# d = np.array({10, 20, 30, 40, 50})
# print(d, type(d))

# e = np.array((10, 20, 30, 40, 50))
# print(e, type(e))

print(len(b))
b[2] = 60
print(b)

b1 = np.append(b, [70, 80, 90])
print(b1)

for i in b:
    print(i)

"""

"""
a = np.array([10, 20, 30, 40, 50, 60, 70, 80])
a1 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# a2 = np.array([[],[]])
print(a)
print(a1)
print(len(a), len(a1))
print(a[1])
print(a1[1][2])
print(a.shape)
print(a1.shape)
print(a1.shape[0])
# print(a2)
a3 = np.array([[10, 20], [40, 50, 60], [70, 80, 90, 100]])
print(a3)
print(a3.shape)


a4 = np.zeros(8)
print(a4)
a4 = np.ones(9)
print(a4)

a5 = a.reshape(2,2,2)
print(a)
print()
print(a5)
a6 = a5.ravel()
print(a6)
"""

# a = np.zeros((8,8))
# print(a)
# b = np.ones((8,8))
# print(b)
"""
c = np.array([1, 0, 1, 0, 1, 0,1, 0])
print(c)
d = c[::-1]
print(d)
e = np.array(c)
for i in range (7):
    if (i%2 == 0):
        # print(c)
        e = np.append(e, d)
    else:
        # print(d)
        e = np.append(e, c)
e = e.reshape(8,8)
print(e)
"""
cb = np.zeros((8,8), dtype=int)


cb[1::2, ::2] = 1
cb[::2, 1::2] = 1
print(cb)
for _ in range (4):
    a,b = map(int,input("Where to place queen:").split())
    cb[a][b] = 9
    print(cb)