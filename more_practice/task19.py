# Task 19: Ekta function flatten_and_average(list_of_lists) likho jeta ekta "list of lists" nibe (jemon [[1,2],[3,4],[5]]), shob number ekshathe kore average ber kore return korbe

list_of_lists = [[1,2], [3,4], [5]]

def flatten_and_average(list_of_lists):
    flat_list = []

    for sublist in list_of_lists:
        for num in sublist:
            flat_list.append(num)
    if len(flat_list) == 0:
        return 0
    total_sum = 0
    for element in flat_list:
        total_sum += element
    return total_sum / len(flat_list)

print("Average of flat list:", flatten_and_average(list_of_lists))