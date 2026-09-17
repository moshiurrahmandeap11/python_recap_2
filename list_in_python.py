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
os.system("cls")

for fruit in fruits:
    print(fruit)



os.system("cls")





# Task 1: Ekta list banao 5 ta number diye। Loop use kore shob number print koro।



numbers = [1,2,3,4,5]

for number in numbers:
    print(number)


os.system("cls")

# Task 2: Ekta list banao 5 ta number diye। Loop diye shob number er sum ber koro।

numbers = [1,2,3,4,5]

total_sum = 0

for number in numbers:
    total_sum = total_sum + number

print("total sum :", total_sum)

os.system("cls")


# Task 3: Ekta list e user theke 5 ta number nao (input diye, loop e), tarpor list ta print koro।

user_list = []

for i in range(7):
    user_input = int(input("Enter number :", ))
    user_list.append(user_input)

print("user inputed number :", user_list)