#!/usr/bin/env python

s = raw_input()

# s_build = ''
# i = 0
# while i < len(s):
#         if i % 2 == 0:
#                 s_build = s_build + s[i]
#         i = i + 1
# print s_build

s_build = ''
largest_multiplier = (len(s)+1)/2

i = 0
while i < largest_multiplier:
       s_build = s_build + s[2*i]
       i = i + 1

print s_build
