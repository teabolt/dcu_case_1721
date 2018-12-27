#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

n = 10 # number of elements to print / sorting (generalisation)

# insertion sort

# i = 1
# while i < len(a):
#    v = a[i]
#    p = i
#    while 0 < p and v < a[p-1]:
#        a[p] = a[p-1]
#        p = p - 1
#    a[p] = v
#    i += 1

# selection sort, because you can sort the first n elements in a list a without going through the whole list(insertion sort needs to).

i = 0
while i < len(a) and i < n:
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j += 1
    tmp = a[p]
    a[p] = a[i]
    a[i] = tmp
    i += 1

i = 0
while i < len(a) and i < n:
    print a[i]
    i += 1