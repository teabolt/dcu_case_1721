#!/usr/bin/env python

import sys

s = sys.argv[1]
total = 0

i = 0
while i < len(s):
    total += int(s[i])
    i = i + 1

print total