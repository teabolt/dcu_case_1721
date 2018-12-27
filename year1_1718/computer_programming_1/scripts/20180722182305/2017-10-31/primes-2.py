#!/usr/bin/env python

# assume there's a list 'a' and a function 'isprime()'

i = 0
while i < len(a) and not isprime(a[i]):
    i += 1

if i < len(a):
    print a[i]