# Task 18: Ekta function sum_of_digits(number) likho jeta ekta number er shob digit er sum ber kore return korbe (jemon 1234 → 1+2+3+4 = 10) — loop diye, % ar // use kore

number = 12345

def sum_of_digits(num):
    total_sum = 0

    while num > 0:
        last_digit = num % 10
        total_sum += last_digit
        num = num // 10
    return total_sum

print("Sum of digits:", sum_of_digits(number))