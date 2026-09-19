# Task 4: Ekta function find_second_largest(numbers) likho jeta list theke 2nd largest number ber kore return korbe (loop diye, sort() use na kore)

numbers = [1,2,3,4,5]

def find_second_largest(numbers):
    largest = 0
    second_number = 0
    for num in numbers:
        if num > largest:
            second_number = largest
            print("second number ", second_number)
            largest = num
            print("largest :", largest)
        elif num > second_number and num != largest:
            second_number = num
            print("second largest :", second_number)
    return second_number

print("second largest number :", find_second_largest(numbers))