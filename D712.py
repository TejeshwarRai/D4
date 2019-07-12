import numpy as np

i1 = np.array([0, 0])
i2 = np.array([0, 1])
i3 = np.array([1, 0])
i4 = np.array([1, 1])

weights = np.array([0.5, 0.5])

theta = 1

def activation(s):
    if s>=theta:
        return 1
    else:
        return 0

def summation(x, w):
    s = np.dot(x, w)
    y = activation(s)
    return y

o1 = summation(i1, weights)
o2 = summation(i2, weights)
o3 = summation(i3, weights)
o4 = summation(i4, weights)

print("For", i1, "|", o1)
print("For", i2, "|", o2)
print("For", i3, "|", o3)
print("For", i4, "|", o4)
