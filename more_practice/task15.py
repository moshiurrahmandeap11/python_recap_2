# Task 15: Ekta function multiplication_table_list(num) likho jeta 1 theke 10 porjonto tar table list hishebe return korbe (print na, list return, jemon table_list(2) → [2,4,6,8,...,20])

def multiplication_table_list(num):
    multi_list = []
    for n in range(1, 11):
        multi_list.append(num * n)
    return multi_list

print("2 er namtar list:", multiplication_table_list(2))