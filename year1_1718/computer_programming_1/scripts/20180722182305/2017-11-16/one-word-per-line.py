#!/usr/bin/env python

import sys

# stdin as one giant string.
s = sys.stdin.read()

# join together separate lines into one string(removed newlines).
a = s.split("\n")
s = " ".join(a)

# separate whitspace(a single space - or more -> general case without argument)-delimited words by newlines.
a = s.split()
s = "\n".join(a)

print s