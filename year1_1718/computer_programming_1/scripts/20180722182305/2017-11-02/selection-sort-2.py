#!/usr/bin/env python

a = []
s = raw_input()

while s != "end":
    a.append(int(s))
    s = raw_input()

i = input()
smallest = i

j = i + 1
while j < len(a):
    if a[j] < a[smallest]:
        smallest = j
    j += 1

print smallest