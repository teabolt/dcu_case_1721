#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
    ## s: "DD/MM/YY Name" change to "YY/MM/DD Name" for lexicographic ordering via date of birth(naturally, if date of birth is the same, then the order depends on the name. Makes sense!)
    s = s[6:8] + "/" + s[3:5] + "/" + s[0:2] + " " + s[9:] # string slices
    a.append(s)
    s = raw_input()

# selection sort

i = 0
while i < len(a):
    # left --- right
    # | sorted  | unsorted. Swap on right, current element(testing against). Swap with smallest.

    # find smallest
    p = i
    j = i + 1
    while j < len(a):
        if a[j] < a[p]:
            p = j
        j += 1

    # swap current with smallest
    tmp = a[i]
    a[i] = a[p]
    a[p] = tmp

    i += 1

i = 0
while i < len(a):
    print a[i][9:]
    i += 1