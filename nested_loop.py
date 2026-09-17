import os
import sys


for i in range(10):
    print("moshiur ", i)
    i = i + 1



os.system("cls")


for i in range(5):
    for j in range(4):
        print("moshiur ", i, j)


os.system("cls")


# Task 1: Ekta simple star pattern print koro:

for i in range(6):
    for j in range(i):
        print("*", end="")
    print("")


os.system("cls")


# Task 2: 1 theke 5 porjonto shob number er multiplication table ekshathe print koro (age tumi 1ta number er table korso, ekhon 1-5 shob koyta):


for i in range(1, 6):
    print("Multiplication Table of", i)
    for j in range(1, 11):
        result = i * j
        print(i, "x", j, "=", result)

os.system("cls")

# Task 3 (mojar): Ekta grid print koro emon:
# 1 2 3
# 4 5 6
# 7 8 9


for i in range(1, 10):
    print(i, end=" ")
    if i % 3 == 0:
        print("")