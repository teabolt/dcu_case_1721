#!/usr/bin/env python

s = raw_input()
s_whitespaceless = ''

i = 0
while i < len(s):
        if not s[i].isspace():
                s_whitespaceless = s_whitespaceless + s[i]
        i = i + 1

print s_whitespaceless
