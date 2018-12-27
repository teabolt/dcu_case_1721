#!/usr/bin/env python

import sys

s = raw_input()
c = sys.argv[1]

i = 0
while i < len(s) and s[i] != c:
    i += 1

if i < len(s):
    print i