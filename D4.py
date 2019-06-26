# creation of containers
instausername = "hello"
time = 3

# updating container
time = 4

# deleting container
del time

print(instausername)
print(id(instausername))
print(hex(id(instausername)))
print(bin(id(instausername)))
print(oct(id(instausername)))

print()


# ================================= #

Johnsage = 30
print(Johnsage, hex(id(Johnsage)))
print(Johnsage, " ", hex(id(Johnsage))) # extra space

Johnysage = 30
print(Johnysage, hex(id(Johnysage)))    # both have same hexid

# Johnysage and Johnsage are reference variables

# copy operation: Reference copy nt Data
JacksAge = Johnysage

# ================================== #

diprice = 100
doprice = 100, 150, 200

print(diprice, hex(id(diprice)), type(diprice))
print(doprice, hex(id(doprice)), type(doprice))
print(doprice[1])


# ================================== #

ag1 = (10,20,30,40,50)      # data not modifiable (IMMUTABLE)
ag2 = [10,20,30,40,50]      # Mutable
ag3 = {10,20,30,40,50}      # Mutable and Unordered ... UNIQUE ... No repetitions

print(ag1, hex(id(ag1)), type(ag1))
print(ag2, hex(id(ag2)), type(ag2))
print(ag3, hex(id(ag3)), type(ag3))

# =================================== #
print()
dish = {"dal": 100, "Murga": 300}

print(dish)
print(hex(id(dish)))
print(type(dish))
