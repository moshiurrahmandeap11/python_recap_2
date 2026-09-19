# Task 3: Ekta function reverse_list(numbers) likho jeta ekta list nibe ar loop diye (built-in reverse() use na kore) reverse kore notun list return korbe

numbers = [1,2,3,4,5]


def reverse_list(numbers_got):
    reverse_number = []
    for num in numbers_got:
        reverse_number.insert(0, num)    
    return reverse_number


print("getting reverse without built-in reverse() ",reverse_list(numbers))