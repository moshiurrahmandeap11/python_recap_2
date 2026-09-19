# Task 16: Ekta function separate_even_odd(numbers) likho jeta ekta list nibe, ar duita alada list return korbe — ekta even numbers er, arekta odd numbers er

numbers = [1,2,3,4,5,6,7,8,9,10]

def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        elif num % 2 != 0:
            odd_numbers.append(num)
    return even_numbers, odd_numbers

print(separate_even_odd(numbers))