#!/usr/bin/env python

s = raw_input()
s_reversed = ''

i = 0
while i < len(s):
        s_reversed = s_reversed + s[len(s)-1-i]
        i = i + 1
        
print s_reversed


