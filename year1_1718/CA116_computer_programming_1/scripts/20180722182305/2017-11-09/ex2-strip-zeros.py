#!/usr/bin/env python

s = raw_input()
while s != "end":
    # assume 's' is a non-negative integer string.
    i = 0
    while i < len(s) and s[i] == "0":
        i += 1
    if i < len(s):
        print s[i:]
    else:
        print "0"
    s = raw_input()