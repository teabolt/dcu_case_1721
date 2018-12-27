#!/usr/bin/env python

a = []

# -- 1. read

s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

# -- 2. sort

i = 0 # visit every item in sequence
while i < len(a): # iterate from start to end(in terms of index)
    
    # divide the list into sorted and unsorted parts:
    p = i # guess the least element in the unsorted sub-list

    j = i # iterate through every item in the unsorted list to get the least item.
    while j < len(a): # go from start of unsorted list to end.
        # check if current least element is actually the least
        if a[j] < a[p]:
            p = j # if not, set the least element to a new value - the current(lesser) element.
        j += 1 # loop counter for j-loop
    # by the end of this p will be the position of the least element in the unsorted list

    # add the smallest element to the sorted list's end. Swap i(start of unsorted list) with p(smallest item inside unsorted list).
    tmp = a[i] # store old i element.
    a[i] = a[p] # swap, give i the value of p.
    a[p] = tmp # give p the old value of i

    i += 1 # loop counter. Move on to checking from the next unsorted item.
# now having gone through all the items, the list is sorted.

# -- 3. median

median = a[len(a) / 2]

print median