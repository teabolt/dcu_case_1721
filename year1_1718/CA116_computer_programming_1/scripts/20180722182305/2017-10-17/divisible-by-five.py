#!/usr/bin/env python

s = raw_input()

while s != "end":
    if s[len(s) - 1] == "5" or s[len(s) - 1] == "0":
        print s
    s = raw_input()