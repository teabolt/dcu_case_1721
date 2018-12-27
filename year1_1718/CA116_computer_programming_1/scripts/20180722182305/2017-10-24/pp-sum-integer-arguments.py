#!/usr/bin/env python

import sys

total = 0

i = 1
while i < len(sys.argv):

    arg = sys.argv[i]
    
    j = 0
    while j < len(arg) and arg[j].isdigit():
        j += 1

    if j == len(arg):
        total = total + int(arg)

    i += 1

print total