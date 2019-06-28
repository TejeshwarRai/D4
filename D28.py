import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""
num = [11,22, 33, 44, 55]
s1 = pd.Series(num)
print(s1)

age = {"john":20,"jim":30,"jack":40,"joe":50}
s2 = pd.Series(age)
print(s2)

print(s1[0])
print(s2["jim"])

print(s1[1:])
print(s1[:3])
print(s1[2:5])

print(s2["jim":])
print(s2["jim":"joe"])
"""
#
# num1 = [10,20, 30, 40, 50]
# num2 = [11,22, 33, 44, 55]
#
# emp1 = {"eid":101, "name":"John", "age":20}
# emp2 = {"eid":102, "name":"Fionna", "age":22}
# emp3 = {"eid":103, "name":"Kia", "age":24}
#
# df1 = pd.DataFrame([num1, num2])
# df2 = pd.DataFrame([emp1, emp2, emp3])
#
# print(df1)
# print()
# print(df2)
# print()
#
# print(df1[0])
# print()
# print(df2["eid"])
#
# print()
# print(df2["eid"][0])
# print(df2[:][:])

# bla = pd.read_csv("file.csv")
"""
y = [10,20,30,40,50]
plt.plot(y)
plt.show()
"""

# x = list(range(0,11))
# y1 = [n for n in x]
# y2 = [n*n for n in x]
# y3 = [n*n*n for n in x]
#
# print(x)
# print(y1)
# print(y2)
# print(y3)
#
# plt.plot(x,y1, label = "y1")
# plt.plot(x,y2, label = "y2")
# plt.plot(x,y3, label = "y3")
# plt.legend()
#
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
#
# plt.title("Polynomial Graphs")
# plt.grid("true")
# plt.grid(True)
#
# plt.xlim(0, 50)
# plt.ylim(0, 2000)
#
# plt.savefig("1st Graph")        # to save graph
# plt.show()

"""
x = np.random.randn(50)
print(x)
plt.hist(x,50)
plt.show()
"""

# a = [1,2,3,4,5,6,]
# b = [12,43,12,65,86,34]
#
# plt.bar(a,b)
# plt.show()

scores = {"a":12,"b":23,"c":42,"d":30,"e":27}
# plt.bar(0, scores["a"])
# plt.bar(1, scores["b"])
for i ,key in enumerate(scores):
    plt.bar(key,scores[key])        # shows key name
    # plt.bar(i,scores[key])        # shows 1,2

plt.xlabel("abc")
plt.ylabel("score")
plt.title("runs")

plt.show()
