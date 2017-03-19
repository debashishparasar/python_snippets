#!/bin/python
def insertionSort(unsorted_list):
    for i in xrange(1,int(m)):
        value = unsorted_list[i]
        j     = i
        while j>0 and unsorted_list[j-1] > value:
            unsorted_list[j] = unsorted_list[j-1]
            j    = j-1
        unsorted_list[j] = value
        print ' '.join(map(str,unsorted_list))

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
