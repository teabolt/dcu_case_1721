#!/usr/bin/env python

original = []
firsties = []
s = raw_input()

while s != "end":
    original.append(s)
    s = raw_input()

i = 0
while i < len(original):
    j = 0
    while j < len(firsties) and original[i] != firsties[j]:
        j += 1
    if j == len(firsties):
        print original[i]
        firsties.append(original[i])
    i += 1