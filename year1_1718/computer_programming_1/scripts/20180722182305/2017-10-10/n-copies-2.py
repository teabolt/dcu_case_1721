#!/usr/bin/env python

s = raw_input()
n = input()

s_copy = (s+"-")*n
print s_copy[:len(s_copy)-1]


