#!/usr/bin/env python
# this shebang is for Linux, not Windows.

import sys

s = sys.argv[1]

# linear search of first capital letter.

i = 0
while i < len(s) and not s[i].isupper(): # keep going as long as character isn't capital.
	i += 1

# found position of first capital or fell of the string's end(in terms of indices).

# find the first non-capital character(end of acronym, exclusive).
# this loop won't run once if i == len(s), so it's not that inefficient if an acronym is not found at all as from the first loop.

j = i + 1
while j < len(s) and s[i].isupper(): # keep going as long as character is uppercase.
	j += 1
	
if i < len(s): # check if haven't fallen off the string's end. 
	print s[i:j] + " " + str(i) # print the acronym as a string slice.