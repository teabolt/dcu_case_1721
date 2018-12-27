#!/usr/bin/env python

import sys

longest_arg = ""

i = 1
while i < len(sys.argv):
    if len(longest_arg) < len(sys.argv[i]):
        longest_arg = sys.argv[i]
    i = i + 1

print longest_arg