# Task 8: Ekta function is_prime(number) likho jeta check korbe number ta prime kina, True/False return korbe। (Hint: 2 theke number-1 porjonto loop chalaye check koro kono division e remainder 0 hoy kina

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print("The number is prime: ",is_prime(7))





# Task 9: Ekta function print_primes(n) likho jeta 1 theke n porjonto shob prime number print korbe (Task 8 er is_prime function ta call kore use koro — eta "function er bhitor function call" shekhabe)

def print_primes(n):
    array_of_primes = []
    for num in range(1, n + 1):       
        if is_prime(num) == True:
            print(num)
            array_of_primes.append(num)
    return array_of_primes
print("array of primes: ",print_primes(20))

my_prime_list = print_primes(20)


my_prime_list.append("apple")


print("after appending string in number list :", my_prime_list)