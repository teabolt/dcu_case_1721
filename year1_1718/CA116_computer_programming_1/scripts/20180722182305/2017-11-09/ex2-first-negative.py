#!/usr/bin/env python

# assume an existing list of integers 'a'
# a = [0, 2, 10, 0, 1, -4, 2, -5, 9]

i = 0
while i < len(a) and 0 <= a[i]:
    i += 1

if i < len(a):
    print a[i]