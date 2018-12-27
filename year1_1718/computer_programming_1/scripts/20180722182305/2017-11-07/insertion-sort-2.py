#!/usr/bin/env python

a = []

s = raw_input()
while s != "end":
    a.append(int(s))
    s = raw_input()

n = input()
a.append(n)

p = len(a) - 1
while 0 < p and n < a[p-1]:
    a[p] = a[p-1]
    p = p - 1

a[p] = n

print a