# Task 17: Ekta function fibonacci(n) likho jeta prothom n ta Fibonacci number (0,1,1,2,3,5,8...) list hishebe return korbe (loop diye)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib_list = [0, 1]

    for i in range(n - 2):
        next_num = fib_list[-1] + fib_list[-2]
        fib_list.append(next_num)
    return fib_list

print("Fibonacci series of 5:", fibonacci(5))