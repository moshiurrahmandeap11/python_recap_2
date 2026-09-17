# Task 8: Ekta list e kichu number rakho (jemon [3, 7, 2, 9, 4])। Loop diye sobcheye choto number ber koro (age Task 4 e boro number korso, ekhon opposite — choto number, min() use na kore)

numbers = [3, 7, 2, 9, 4]

small_num = numbers[0]

for number in numbers:
    if number < small_num:
        small_num = number

print("small number from the list :", small_num)