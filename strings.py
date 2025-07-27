# declare string  ||  Stings are not mutable
name = "Tasin"
# -----------------------------------------------------





# -----------------------------------------------------

# slicing string
shortName = name[0:3] # It start from index 0 and slice the string to index 2. 

print(shortName)

# -----------------------------------------------------






# -----------------------------------------------------

# Show 1 character from string
character1= name[0]
print(character1)

# -----------------------------------------------------





# -----------------------------------------------------

#  Negative Slicing 

print(name[0:3]) # is will show Tas
print(name[-5: -2]) # is will show Tas


    #     T   a   s   i   n
    #     0   1   2   3   4
    #    -5  -4  -3  -2  -1


# -----------------------------------------------------




# -----------------------------------------------------

print(name[:3]) # it means start from 0 and end 2  (Tas)
print(name[3:]) # it means start from 4 and end on length size. (in)

# -----------------------------------------------------






# -----------------------------------------------------

# Slicing with skip value: 

a = "abcdefghijklmnopqrstuvwxyz"

print(a[1:16:3])  # a[start value : end value (n-1) : skipping value]


# -----------------------------------------------------





# -----------------------------------------------------

#String Functions:

print(len(name)) # it will shwo the length of the string
 
name2 = "Tanjid"
print(name2.endswith("jid"))  # It will give true false value if string value its ends with sin
print(name2.startswith("Tan"))  # It will give true false value if string value its starts with Tas

b = "ahammed"
print(b.capitalize())  # It will capitalize only the 1st character

full_name = "Tanjid ahammed Tasin"
print(full_name.find("ahammed"))  # it return the index of starting point of that word.


print(full_name.replace("ahammed" , ""))  # it will replace the ahammed word to "" .
print(full_name.replace("ahammed" , "python"))  # it will replace the ahammed word to python .

# -----------------------------------------------------
