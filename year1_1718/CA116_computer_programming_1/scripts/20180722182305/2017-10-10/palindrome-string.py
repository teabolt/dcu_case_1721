#!/usr/bin/env python

s = raw_input()

i = 0
while i < (len(s)/2) and s[i] == s[len(s)-1-i]:
     i = i + 1   

if len(s)/2 <= i :
        print s
