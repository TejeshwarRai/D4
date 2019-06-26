"""
# qwe = 'Johns'
# qwe = 'John\'s'
# qwe = "John's"
qwe = r'John\'s'  # r or R (Raw string)
print(qwe)

mes = "Hi" \
        "hello" \
        "bye"
print(mes)
"""


# qo = """Hi
# Hello uhkjgu hjmbnb gjv iugkg fj gk
# jvhmv,bjmgu kbhmjg kuh"""               # not a cmmnt in case of strings
# print(qo)

"""nm = "Jpj jkol"
print(nm, type(nm), hex(id(nm)))
print(len(nm))
print(min(nm))      # space will be shoen (if there)
print(max(nm))
print(nm[1])
print(nm[len(nm)-1])
print(nm[1:3])
print("t" in nm)

email = "hf@hj.com"

if ("@" in email) and ("." in email):
    print("valid")
else:
    print("invalid")


# String formatting
nm = "Fionna"
ag = 65   
print("Wwlcome %s"%nm)
print("Age %d"%ag)
print("%s %d "%(nm, ag))
print(nm, ag)

print("hi , {}  ({})".format (nm, ag))
"""
# ================================== #

# for i in range(0,11,1):
#  print("{} * {} = {}".format(7, i, 7*i))
"""
nm = "jkij klk"
bnm = nm.upper()
print(nm)
print(bnm)

vbnm = nm.capitalize()      # 1st alphabet capital
print(vbnm)
"""

"""press ctrl shift together to move lines"""

# abc = ab.replace('J', 'k')        # (replaces J by k)(string)
# num = ab.count("J", 0, len(ab))   #counts occurrences
# dat = ab.split(",")               # split on basis of ,
# print(ab.strip())                 # to eliminate space

"""
salutation = "mr"
fnme = "Fuddu"
name = salutation + fnme
print(name)
"""
"""quote = "hgu Jaj Jiadhhk "
# dat = list(quote)
# dat = tuple(quote)
# dat = set(quote)
# dat = dict(quote)             ?explore
# print(dat)
print(quote[13:5:-1])

for i in range(len(quote)-1, -1, -1):
    print(quote[i], end=" ")
"""



A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
F = {1, 2, 3}
C = A | B
D = A & B
E = A - B
print(C)
print(D)
print(E)

print(F.issubset(A))
print(A.issuperset(F))

print(A.union(B))
print(B.difference(A))
print(A.intersection(F))
# ?explore symmetric difference
