# Task 21: Ekta function most_frequent(numbers) likho jeta list e sobcheye beshi bar repeat hoya number ta ber kore return korbe (jemon [1,2,2,3,2,4] → 2)

numbers = [1,2,2,3,2,4]

def most_frequent(numbers):
    common_number = numbers[0]
    max_count = 0
    for num in numbers:
        current_count = 0
        for check_num in numbers:
            if check_num == num:
                current_count += 1
        if current_count > max_count:
            max_count = current_count
            common_number = num
    return common_number
        

print("Most frequent number:", most_frequent(numbers))