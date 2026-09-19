# Task 10: Ekta function list_of_squares(numbers) likho jeta ekta list nibe, protita number er square kore notun list banaye return korbe (jemon [1,2,3] → [1,4,9])

numbers = [1,2,3]

def list_of_sqaures(numbers):
    square_list = []
    for num in numbers:
        print(num)
        square_list.append(num ** 2)
    return square_list

print("square list of number :",list_of_sqaures(numbers))