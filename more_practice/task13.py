# Task 13: Ekta function count_occurrences(numbers, target) likho jeta list e ekta specific number koybar ache seta count kore return korbe

numbers = [1,2,3,4,4,5]

def count_occurrences(numbers, target):
    count_num = 0
    for num in numbers:
        if num == target:
            count_num += 1
    return count_num

print("Target ache total:", count_occurrences(numbers, 4), "bar")
