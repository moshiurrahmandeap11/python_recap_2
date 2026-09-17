import os,sys

# Task 6: Ekta function likho factorial(n) jeta n! (factorial) calculate kore return korbe। (e.g., factorial(5) = 5×4×3×2×1 = 120)

def factorial(n):
    total = 1
    for i in range(n,0, -1):
        total = total * i
    return total
        

print(factorial(5))


os.system("cls")

# Task 7: Ekta function likho max_of_three(a, b, c) jeta 3ta number er moddhe sobcheye boro ta return korbe (loop na, if-else use koro)।

def max_of_three(a,b,c):
    big = a

    if b > big:
        big = b
    if c > big:
        big = c
    return big

print(max_of_three(1,2,3))

os.system("cls")



# Task 8 (default parameter): Ekta function likho power(base, exponent=2) — jodi exponent na dao, default 2 (square) hishebe calculate hobe:


def power(base, exponent=2):
    total = base ** exponent
    return total

print(power(2, 3))