#  Tuples is an immutable list in python.


# creating tuple
a = (1,2,3,4)  
print(type(a))

# write single value in tuple

b = (1) #This is not a tuple
print(type(b))

c = (1,) #This is a tuple. whe have to declare single value with comma
print(type(c))


d = (1,2,3,4,5,6,7,8,9,10)
print(d[0])

# d[0] = 100
# print(d)  can't change the value of tuple. tuple is immutable



# =======================================================


# Methods of tuple

abc = (1,2,3,2,2, "Tasin", "Tanjid", False)

print(abc.count(2))


i = abc.index(2) # it will return the index of 2
print(i)