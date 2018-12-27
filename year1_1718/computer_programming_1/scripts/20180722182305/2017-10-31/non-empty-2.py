#!/usr/bin/env python

# assume list 'a' exists

i = 0
while i < len(a) and a[i] == "":
    i += 1

if i < len(a):
    print a[i]