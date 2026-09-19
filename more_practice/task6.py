# Task 6: Ekta function remove_duplicates(numbers) likho jeta list theke duplicate value remove kore notun list return korbe (loop diye, set() use na kore)

numbers = [1,2,3,3,4,5,6,7,7,8]

def remove_duplicates(numbers):
    remove_dupli = []
    for num in numbers:
        if num not in remove_dupli:
            remove_dupli.append(num)
    return remove_dupli

print("after remove dupli ",remove_duplicates(numbers))