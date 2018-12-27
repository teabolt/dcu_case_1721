#!/usr/bin/env python

import sys

ns = sys.stdin.readline().rstrip() # read integers(n) as strings(s), trailing newlines removed.
while 0 < len(ns):
    i = 0
    while i < len(ns) and ns[i] == "0":
        i += 1
    if i < len(ns):
        print ns[i:]
    else:
        print "0"
    ns = sys.stdin.readline().rstrip()