# Task 20 (Challenge — sob combine): Ekta function analyze_numbers(numbers) likho jeta ekta list nibe ar ekshathe ei shob calculate kore return korbe (dictionary hishebe return korle valo hoy, na parle just print koro):

# Total sum
# Average
# Largest number
# Smallest number
# Koyta even, koyta odd


numbers = [1, 2, 3, 4, 5]

def analyze_numbers(numbers_got):
    
    if not numbers_got:
        return {"sum": 0, "avg": 0, "max": 0, "min": 0, "even": 0, "odd": 0}
        

    total_sum = 0
    largest = 0  
    smallest = 0  
    even_count = 0
    odd_count = 0
    

    for num in numbers_got:

        total_sum += num
        

        if num > largest:
            largest = num
            

        if num < smallest:
            smallest = num
            

        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            

    average = total_sum / len(numbers_got)
    

    analysis_result = {
        "Total Sum": total_sum,
        "Average": average,
        "Largest Number": largest,
        "Smallest Number": smallest,
        "Even Count": even_count,
        "Odd Count": odd_count
    }
    
    return analysis_result


print("Ultimate Analysis Matrix:\n", analyze_numbers(numbers))
