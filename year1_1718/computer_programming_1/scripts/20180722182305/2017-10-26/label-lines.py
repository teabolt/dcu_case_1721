#!/usr/bin/env python

s = raw_input()
a = []

while s != "end":
    a.append(s)
    s = raw_input()

i = 0
while i < len(a):
    print i, len(a), a[i]
    i += 1