#!/usr/bin/env python

import sys

s = raw_input()
c = sys.argv[1]

i = 0
while i < len(s):
    if s[i] == c:
        print i
    i += 1