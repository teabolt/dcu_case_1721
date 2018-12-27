#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
    a.append(int(s)) # assume 's' is convertable string integer.
    s = raw_input()

# loop invariant: a[0:i] is sorted

i = 1
while i < len(a):
    v = a[i]
    p = i
    while p > 0 and v < a[p-1]:

        a[p] = a[p-1]
        p -= 1
    a[p] = v
    i += 1

i = 0
while i < len(a):
    print a[i]
    i += 1