import os
import sys

def great(name):
    print(f"Hello, {name}!")

great("Rahman")

def table(num):
    for j in range(1, 11):
        print(num, "x", j, "=", num*j)

table(5)   # 5 er table
table(7)   # 7 er table


os.system("cls")

# Task 1: Ekta function likho greet(name) jeta print korbe "Hello, [name]! Kemon acho?"

def greet(name):
    print("Hello, " + name + "! Kemon acho?")

greet("Rahman")


os.system("cls")

# Task 2: Ekta function likho add(a, b) jeta return korbe duita number er sum (print na, return)। Tarpor eta call kore result print koro.

def add(a, b):
    return a + b

result = add(5, 7)
print("Total:", result)


os.system("cls")


# Task 3: Ekta function likho is_even(number) jeta check korbe number ta even naki odd, ar True/False return korbe।

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print("Is 4 even?", is_even(4))


os.system("cls")


# Task 4: Age tumi loop diye 1 theke N porjonto sum ber koresile — ekhon eta function banao: sum_upto(n) jeta 1 theke n porjonto sum return korbe।


def sum_upto(n):
    total = 0
    for i in range(1, n + 1):
        total += i
        print(f"Adding {i}, current total: {total}")
    return total

print("Sum up to 15:", sum_upto(15))

os.system("cls")


# Task 5 (function + loop combine): Ekta function likho print_table(num) jeta shei number er multiplication table print korbe (1 theke 10 porjonto) — ei function ta 2-3 ta alada number diye call koro (jemon print_table(5), print_table(8))

def print_table(num):
    print("Multiplication Table for", num)
    for j in range(1, 11):
        print(num, "x", j, "=", num * j)

print_table(5)