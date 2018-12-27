#!/usr/bin/env python

import sys

with open(sys.argv[1], "w") as f_in:
    f_in.write("Hello world." + "\n")