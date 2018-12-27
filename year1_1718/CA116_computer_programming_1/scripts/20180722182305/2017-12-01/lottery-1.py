#!/usr/bin/env python

n = 3
prizes = [0, 1, 5, 100]

import sys
a = sys.stdin.readlines()

draw = {}

i = 1
while i < len(sys.argv):
    draw[sys.argv[i]] = True
    i += 1

i = 0
while i < len(a):
    tokens = a[i].split()
    count = 0
    j = 0
    while j < n:
        if tokens[j] in draw:
            count += 1
        j += 1

    print prizes[count]
    i += 1