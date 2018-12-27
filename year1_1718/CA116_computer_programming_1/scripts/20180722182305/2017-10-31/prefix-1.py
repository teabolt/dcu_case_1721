#!/usr/bin/env python

# assume there exists a list 'a', and a string 's'.

i = 0
while i < len(a):
    if a[i][0:len(s)] == s:
        print a[i]
    i += 1