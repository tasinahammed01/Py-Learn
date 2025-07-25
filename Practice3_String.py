# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.

# name = input("Enter your name:")

# print("Good Afternoon", name)

# --------------------------------------------------------------


# 2. Write a program to fill in a letter template given below with name and date.
# letter = ***
# Dear < Name|›,
# You are selected!
# < |Date| >


# letter = ''' Dear |Name|,
#              You are selected!
#              |Date|'''

# print(letter.replace("|Name|" , "Tasin").replace("|Date|" , "01 July 2025"))




# --------------------------------------------------------------


# 3. Write a program to detect double space in a string.


# text = "My  name is  Tanjid ahammed  Tasin"

# print(text.find("  "))


# --------------------------------------------------------------

# 4. Replace the double space from problem 3 with single spaces.




# text = "My  name is  Tanjid ahammed  Tasin"

# print(text.replace("  ", " "))




# --------------------------------------------------------------

# 5. Write a program to format the following letter using escape sequence characters.
# letter = " Dear Tasin, this python is nice. Thanks !"

letter = " Dear Tasin,\n\tthis python is nice.\nThanks !"

print(letter)