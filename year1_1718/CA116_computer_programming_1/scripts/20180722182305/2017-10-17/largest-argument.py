#!/usr/bin/env python

import sys

largest_arg = int(sys.argv[1])

i = 2
while i < len(sys.argv):
    if largest_arg < int(sys.argv[i]):
        largest_arg = int(sys.argv[i])
    i = i + 1

print largest_arg