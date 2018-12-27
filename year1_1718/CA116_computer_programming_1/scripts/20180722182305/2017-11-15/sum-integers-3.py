#!/usr/bin/env python

import sys

total = 0

i = 1
while i < len(sys.argv):
    with open(sys.argv[i]) as f_in:
        s = f_in.readline()
        while 0 < len(s):
            total += int(s)
            s = f_in.readline()
    i += 1

print total