import time
import random

this_list  = random.sample(range(100),60)
print "Orginal List...."
print this_list

"""
Divide and conquer recursively
"""
def merge_sort(unsorted_list):
    list_length = len(unsorted_list)
    if list_length == 1:
        return unsorted_list

    sublist1 = unsorted_list[0:list_length/2]
    sublist2 = unsorted_list[list_length/2:]


    sublist1 = merge_sort(sublist1)
    sublist2 = merge_sort(sublist2)
    return mergeit(sublist1,sublist2)

"""
Merge given two lists in sorted order of their elements
"""
def mergeit(list1,list2):
    length = min(len(list1),len(list2))

    merged_list = list()

    while (len(list1) > 0 and len(list2) > 0):
        if list1[0] > list2[0]:
            merged_list.append(list2[0])
            del list2[0]
        else:
            merged_list.append(list1[0])
            del list1[0]

    if len(list1) > len(list2):
        merged_list.extend(list1)
    elif len(list2) > len(list1):
        merged_list.extend(list2)
    return merged_list

this_list = merge_sort(this_list)
print "Sorted List...."
print this_list
