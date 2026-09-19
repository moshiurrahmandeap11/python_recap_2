# Task 8: Ekta function is_prime(number) likho jeta check korbe number ta prime kina, True/False return korbe। (Hint: 2 theke number-1 porjonto loop chalaye check koro kono division e remainder 0 hoy kina

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print("The number is prime: ",is_prime(7))