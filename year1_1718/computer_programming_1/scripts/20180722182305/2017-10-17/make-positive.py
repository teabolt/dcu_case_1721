#!/usr/bin/env python

s = raw_input()

while s != "end":
    s_dig = ""
    
    i = 0
    while i < len(s):
        if s[i].isdigit():
            s_dig += s[i]
        i += 1
    
    print s_dig
    s = raw_input()