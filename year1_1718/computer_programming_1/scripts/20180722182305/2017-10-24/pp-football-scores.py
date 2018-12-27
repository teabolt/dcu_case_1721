#!/usr/bin/env python

import sys

score = int(sys.argv[1])

goals_possible = score / 3 + 1

i = 0
while i < goals_possible:
    print i, (score - 3*i)
    i += 1