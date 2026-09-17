# Task 11 (check existence): Ekta list banao kichu fruit diye। User theke ekta fruit name input nao, check koro seta list e ache kina in keyword diye

fruits = ["apple", "grapes", "tometo", "orange"]

user_input = input("Enter a fruit name :").lower()

if user_input in fruits:
    print("Fruit in the list")
else:
    print("Fruit isn't in the list")