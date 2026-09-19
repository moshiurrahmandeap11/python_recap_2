# Task 12: Ekta function merge_and_sort(list1, list2) likho jeta duita list combine kore, tarpor loop diye (nijer logic e, sort() use na kore — bubble sort try koro) ascending order e sajiye return korbe


list1 = [1,2,3]
list2 = [6,5,4]

def merge_and_sort(list1, list2):
    combine_list = list1 + list2
    n = len(combine_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if combine_list[j] > combine_list[j + 1]:
                combine_list[j], combine_list[j + 1] = combine_list[j + 1] , combine_list[j]
        return combine_list

print(merge_and_sort(list1, list2))