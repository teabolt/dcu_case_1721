#!/usr/bin/env python

list_1 = []
list_2 = []
a = []

s = raw_input()
while s != "end":
    list_1.append(int(s))
    s = raw_input()

s = raw_input()
while s != "end":
    list_2.append(int(s))
    s = raw_input()

a = list_1 + list_2

# selection sort

i = 0 # go through each element in 'a'. 'a[0:i]'(left) is sorted.
while i < len(a):
    # find smallest element's position 'p' in 'a[j:i]'(right)
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j += 1

    # swap smallest
    tmp = a[i]
    a[i] = a[p]
    a[p] = tmp

    i += 1

i = 0
while i < len(a):
    print a[i]
    i += 1