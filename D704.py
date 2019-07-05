import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

"""
    Linear regression
    Data is known before hand
    Hence, supervised learning
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]
        
    Eqn of regression line
    y = b0 + b1x
    
    to find slope of line b1
    
    Step 1:
    ----------------------------------------------------------
    x    |  y  | x-mean(x) | y-m(y) | sq(x-mx)  | (x-mx)(y-my)
    ----------------------------------------------------------
    1       2       -2       -2         4            4
    2       4       -1        0         1           -4
    3       5        0        1         0            0
    4       4        1        0         1            0
    5       5        2        1         4            2   
    
    Step 2:
    Sum of sq(x-mx): 10
    Sum of (x-mx)(y-my): 6
    
    b1 = Slope of line
    b1 = [Sum of (x-mx)(y-my)]/[Sum of sq(x-mx)]
    b1 = 0.6
    
    eqm => y = b0 + 0.6x
        put mean value
    4 = b0 + (0.6*3)
    b0 = 2.2
    
    so, y = 2.2 + (0.6)x
    
    Step 3:
    Calculate errors 
    if errors ase less then ok else optimize
    types:
        1.MSE
        2.R2
        3.VARIANCE
        
    For MSE:
    Substitute original value of x and compute y with equation of line
    
    -------------------------------------------------
    X   Y    Y'     Y-MY    Sq(Y-MY)  Y'-MY  Sq(Y'-MY)
    -------------------------------------------------
    1   2   2.8     -2      4         -1.2      1.44
    2   4   3.4      0      0         -0.6      0.36
    3   5   4        1      1            0      0
    4   4   4.6      0      0          0.6      0.36
    5   5   5.2      1      1          1.2      1.44
    -------------------------------------------------
"""
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
data = stats.linregress(x, y)
print("Slope of line:", data[0])
print("Intercept of line:", data[1])

maxX = np.max(x) + 10
minX = np.min(x) - 10
X = np.linspace(minX, maxX, 100)
Y = data[1] + data[0]*X

plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
# plt.plot(x,y,"o")
# plt.plot(x, y, "o", color="r", label="Data Points")
plt.plot(X, Y, color="r", label="Regression Line")
plt.scatter(x, y, color="b", label="Data points")
plt.legend()
plt.show()

"""
a = np.empty((0,3),int)
a = np.append(a, np.array([[1, 2, 3]]), axis=0)
print(a)

# a = np.array([])
# a = np.hstack((a, np.array([1, 2, 3])))
# print(a)
"""

