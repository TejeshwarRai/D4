"""
for i in range (20):
    if i in range(15,18):
        continue
    print(i,end=" ")
"""
import numpy as np
a = np.arange(10,21)
print(a)
print(a.shape)
print(a.ndim)       # dimension

print()

a2 = np.arrange(3,2,3)
print(a2)