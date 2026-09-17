import os,sys
# for loop

for i in range(1, 11):
    even_print = i % 2 == 0
    if even_print:
        print(i, "is an even number.")


# after learning 
for i in range(1,11):
    if i % 2 == 0:
        print(i, "is an even number.")


os.system("cls")

# while loop
count = 0
while count < 1000000000000000000000000000000:
    print(count, "is less than 10")
    count += 1
    if(count == 10000):
        break



os.system("cls")


# Loop Task 1: 1 theke 20 porjonto shob number print koro while loop diye (for loop na, ei bar while diye koro, practice er jonno)

count = 1
while count <= 20:
    print(count)
    count += 1


os.system("cls")


# Loop Task 2: Ekta number nao user theke, tar table (multiplication table) print koro 1 theke 10 porjonto:

number = int(input("Enter a number to print its multiplication table: "))

multiplier = 1

while multiplier <= 10:
    result = number * multiplier
    print(number, "x", multiplier, "=", result)
    multiplier += 1



os.system("cls")


# Loop Task 3: 1 theke N porjonto shob number er sum ber koro (loop use kore, N ta user input)

N = int(input("Enter a number N to calculate the sum from 1 to N: "))
sum = 0
i = 1
while i <= N:
    sum = sum + i
    i = i + 1

    print("Current sum after adding", i-1, "is:", sum)

print("The sum of numbers from 1 to", N, "is:", sum)


os.system("cls")


# Loop Task 4: Ekta string nao (jemon "hello"), loop diye protita letter alada line e print koro

text = input("Enter a quote: ")

letter_count = 0
while letter_count < len(text):
    print(text[letter_count])
    letter_count += 1


os.system("cls")


# Loop Task 5 (thoda tough): 1 theke 100 porjonto shob number er moddhe 3 diye divide hoy emon shob number print koro, kintu 15 diye divide hole "FizzBuzz" print koro (eta classic problem, mojar!)


number = 1
while number <= 100:
    if number % 15 == 0:
        print(number, "FizzBuzz")
    elif number % 3 == 0:
        print(number, "is divisible by 3")
    number += 1