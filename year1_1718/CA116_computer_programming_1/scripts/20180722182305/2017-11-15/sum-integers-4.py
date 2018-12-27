#!/usr/bin/env python

import sys

total = 0

i = 1
while i < len(sys.argv):
    with open(sys.argv[i]) as f_in:
        s = f_in.read()
        a = s.split()
        j = 0
        while j < len(a):
            total += int(a[j])
            j += 1
    i += 1

print total