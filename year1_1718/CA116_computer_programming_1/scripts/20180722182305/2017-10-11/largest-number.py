#!/usr/bin/env python

largest_n = input()

i = 0
while i < 4:
    n = input()
    if largest_n < n:
        largest_n = n
    i = i + 1

print largest_n
