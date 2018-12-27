#!/usr/bin/env python

# assume list 'a'

counter = 0

i = 0
while i < len(a):
    if a[i] != "":
        counter = counter + 1
    i += 1

print counter