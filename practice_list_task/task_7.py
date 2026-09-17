# Task 7: Ekta list e 5 ta number rakho। Loop diye koyta even number ache ta count koro।

numbers = [10, 20, 39, 49, 50]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

count_even_numbers = len(even_numbers)
print("Total even numbers :", count_even_numbers)



# another way

numbs = [1,2,3,4,5]

count_even = 0

for numb in numbs:
    if numb % 2 == 0:
        count_even = count_even + 1

print("another way result :", count_even)