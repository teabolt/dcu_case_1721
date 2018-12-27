#!/usr/bin/env python

# assume list 'a' and string 's' exist.

i = 0
while i < len(a) and a[i][0:len(s)] != s:
    i += 1

if i < len(a):
    print a[i]