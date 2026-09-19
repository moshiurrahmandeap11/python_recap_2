# Task 5: Ekta function count_positive_negative(numbers) likho jeta list e koyta positive ar koyta negative number ache, dutai count kore return korbe (2ta value return korte hobe)

numbers = [-3,-2,-1,0,1,2,3]

def count_positive_negative(numbers):
    positive = 0
    negative = 0
    for num in numbers:
        if num > 0:
            positive += 1
        elif num < 0:
            negative +=1
    return positive,negative


print("positive count and negative count :", count_positive_negative(numbers))