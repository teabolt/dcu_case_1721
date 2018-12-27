#!/usr/bin/env python

import sys

with open(sys.argv[1], "w") as f_in:
    i = 2
    while i < len(sys.argv):
        f_in.write(sys.argv[i] + "\n")
        i += 1