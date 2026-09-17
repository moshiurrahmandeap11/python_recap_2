fruits = ["apple", "pinapple", "tometo", "guava"]

print(fruits[1])

# to print a list length
print(len(fruits))

# append something in a list
append = fruits.append("orange")
print(fruits)
print(len(fruits))

# remove something in a list
remove = fruits.remove("apple")
print(fruits)
print(len(fruits))

import os
# os.system("cls")

for fruit in fruits:
    print(fruit)