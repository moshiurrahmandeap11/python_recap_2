# Task 11: Ekta function find_index(numbers, target) likho jeta list e ekta specific value kon index e ache ta ber kore return korbe (loop diye, .index() use na kore)। Na pele -1 return korবে


numbers = [1,2,3,4,5]

def find_index(numbers, target):

    for i, num in enumerate(numbers):
        if num == target:
            return i
    return -1

print("Target er index hocche:", find_index(numbers, 4))
