#!/usr/bin/env python

import sys

s = sys.stdin.readline()
while 0 < len(s):
    s = s.strip() + "\n" # make sure every line has one and exactly one newline character at the end.
    a = s.split("/")
    sys.stdout.write(a[len(a)-1])
    s = sys.stdin.readline()