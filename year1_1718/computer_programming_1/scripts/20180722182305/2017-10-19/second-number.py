#!/usr/bin/env python

import sys

s = sys.argv[1]

i = 0
while i < len(s) and (not s[i].isdigit()):
    i += 1

j = i
while j < len(s) and s[j].isdigit():
    j += 1

k = j
while k < len(s) and (not s[k].isdigit()):
    k += 1

z = k
while z < len(s) and s[z].isdigit():
    z += 1

if i < len(s) and j < len(s) and k < len(s) and z < len(s):
    if s[z] == s[len(s) - 1]:
        print s[k:z+1], k
    else:
        print s[k:z], k