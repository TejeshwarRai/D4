"""
for i in range (20):
    if i in range(15,18):
        continue
    print(i,end=" ")
"""
"""
import numpy as np
a = np.arange(10,21)
print(a)
print(a.shape)
print(a.ndim)       # dimension

print()
"""


"""==============================================================="""
import numpy as np

# Explore : asarray vs array :)
"""
arr = np.arange(10, 51, 3)
print(arr)
print(type(arr))
print(arr.shape)
print(arr.ndim)

# Access Array Elements
print(arr[1])
print(arr[-1])

# Slicing
print(arr[:3])
print(arr[:5])
print(arr[3:5])

slices = slice(1, 20, 2)
print(slices)
print(arr[slices])

arr2D = np.array([(1, 2, 3), (3, 4, 5), (6, 7, 8)])
print(arr2D)
print(arr2D.shape)
print(arr2D.ndim)

print(arr2D[0][1])      # 2

print("................")

print(arr2D[0:2])       # (1, 2, 3), (3, 4, 5)

print("................")

print(arr2D[0][1])  # 2
print(arr2D[0, 1])  # 2

print(arr2D[0:2, 0:2])  #(1,2).(3,4)
"""
'''
arr1 = np.array([(8,9), (10, 12), (13, 14)])
print(arr1[0:2, 1])

arr2 = np.array([10, 20, 30])
print(arr2.min())
print(arr2.max())
print(arr2.sum())

arr3 = np.array([(1, 2, 3), (4, 5, 6)])
print(arr3.sum(axis=0))
print(arr3.sum(axis=1))

arr4 = np.array([(4, 9, 16), (11, 13, 15)])
print(np.sqrt(arr4))
print(np.std(arr4))


arr5 = np.array([(1, 2, 3), (3, 4, 5)])
arr6 = np.array([(1, 2, 3), (3, 4, 5)])

print(arr5 + arr6)
print(arr5 - arr6)
print(arr5 * arr6)
print(arr5 / arr6)
print(arr5 // arr6)

X = np.array([(1, 2, 3), (4, 5, 6)])
Y = np.array([(1, 1, 1), (0, 0, 0)])
print(np.vstack((X,Y)))
print(np.hstack((X,Y)))

Z = np.arange(0, 21, 3)
print(np.sin(Z))
print(np.log10(Z))
'''

