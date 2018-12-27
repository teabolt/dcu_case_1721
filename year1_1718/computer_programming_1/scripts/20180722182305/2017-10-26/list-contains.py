#!/usr/bin/env python

# a = []
# s = raw_input()
# 
# while s != "end":
#     a.append(s)
#     s = raw_input()
# 
# s = raw_input()

i = 0
while i < len(a) and a[i] != s:
    i += 1

print i < len(a)