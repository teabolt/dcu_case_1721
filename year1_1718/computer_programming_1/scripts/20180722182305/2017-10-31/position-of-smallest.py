#!/usr/bin/env python

# assume there's a list 'a' (non-empty, integers)

smallest = 0

i = 1
while i < len(a):
    if a[i] < a[smallest]:
        smallest = i
    i += 1

print smallest