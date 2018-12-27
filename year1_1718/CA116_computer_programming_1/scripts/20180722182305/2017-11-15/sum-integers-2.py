#!/usr/bin/env python

import sys

total = 0

with open(sys.argv[1]) as f_in:
    s = f_in.readline()
    while 0 < len(s):
        total += int(s)
        s = f_in.readline()

print total