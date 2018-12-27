#!/usr/bin/env python

import sys

s = sys.argv[1]

i = 0
while i < len(s) and (not s[i].isdigit()):
    i += 1

j = i
while j < len(s) and s[j].isdigit():
    j += 1

if i < len(s) and j < len(s):
    print s[i:j], i
elif i < len(s) and (not j < len(s)):
    print s[i:j+1], i