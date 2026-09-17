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

# for i in range(5):
#     user_input = int(input("Enter number :", ))
#     user_list.append(user_input)

# print("user inputed number :", user_list)


os.system("cls")


# Task 4: Ekta list theke sobcheye boro number ber koro (loop diye, built-in max() use na kore)।

num_list = [1,2,3,4,5]

big_num = num_list[0]

for nums in num_list:
    if nums > big_num:
        big_num = nums

print("big number from the list :", big_num)

os.system("cls")


# Task 5 (function + list combine): Ekta function likho average(numbers_list) jeta ekta list nibe ar tar average return korbe

def average(numbers_list):

    total_func_num = 0

    for func_num in numbers_list:
        total_func_num = total_func_num + func_num
    average_func_result = total_func_num / len(numbers_list)
    return average_func_result


numbe_list = [1,3,6,9]
result = average(numbe_list)
print("The average is :", result)