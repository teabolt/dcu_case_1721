#!/usr/bin/env python

import sys

s = sys.argv[1]
s_digits = ""

i = 0
while i < len(s):
    if s[i].isdigit():
        s_digits += s[i]
    i += 1

print s_digits