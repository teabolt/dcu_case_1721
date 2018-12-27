#!/usr/bin/env python

import sys

s = sys.argv[1]

i = 0
while i < len(s) and s[i].isspace():
    i += 1

if i < len(s):
    print i
else:
    print -1