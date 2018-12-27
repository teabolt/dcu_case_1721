#!/usr/bin/env python

import sys

total = 0

s = sys.stdin.readline().strip()
while 0 < len(s):
    total += int(s)
    s = sys.stdin.readline().strip()

sys.stdout.write(str(total) + "\n")
# print total