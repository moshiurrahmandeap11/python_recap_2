# Task 7: Ekta function sum_of_squares(n) likho jeta 1² + 2² + 3² + ... + n² er sum return korbe (loop use kore)

def sum_of_squares(n):
    total_sum = 0
    for i in range(1, n+1):
        total_sum += i ** 2
    return total_sum

print("total sum :",sum_of_squares(5))