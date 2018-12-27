#!/usr/bin/env python

import sys

f = sys.argv[1]

i = 0
while i < len(f) and f[i] != ".":
    i += 1

if i < len(f):
    print f[:i]
    print f[i+1:]