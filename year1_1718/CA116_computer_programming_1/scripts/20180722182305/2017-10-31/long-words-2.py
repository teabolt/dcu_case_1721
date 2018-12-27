#!/usr/bin/env python

# assume an existing list 'a'

i = 0
while i < len(a) and len(a[i]) < 6:
    i += 1

if i < len(a):
    print a[i]