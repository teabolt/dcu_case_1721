#!/usr/bin/env python

a = []
s = raw_input()

while s != "end":
    a.append(int(s))
    s = raw_input()

i = 0
while i < len(a):
    if a[i] % 2 == 0:
        print a[i]
    i += 1

i = 0
while i < len(a):
    if a[i] % 2 != 0:
        print a[i]
    i += 1