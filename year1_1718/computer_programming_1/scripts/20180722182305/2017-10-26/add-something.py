#!/usr/bin/env python

a = []
s = raw_input()

while s != "end":
    a.append(int(s))
    s = raw_input()

n = input()

i = 0
while i < len(a):
    print a[i] + n
    i += 1