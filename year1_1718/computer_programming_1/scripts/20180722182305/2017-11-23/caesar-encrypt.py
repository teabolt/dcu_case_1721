#!/usr/bin/env python

import sys

# Build a key for the cipher.
alpha1 = "abcdefghijklmnopqrstuvwxyz" # split into two parts.
alpha2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
r = 13 # number of (right shift) rotations around the alphabet. 0 - stays same. 1 - goes to the very next letter, eg: a -> b, b -> c...
translation = {}

# To generalise, get list slices alpha1 and alpha2 of the overall alphabet, and iterate over all the slices.
i = 0
while i < len(alpha1):
    translation[alpha1[i]] = alpha1[(i+r)%26]
    i += 1

i = 0
while i < len(alpha2):
    translation[alpha2[i]] = alpha2[(i+r)%26]
    i += 1

# Read lines.

lines_s = sys.stdin.read()

# Output encrypted lines, character by character.

i = 0
while i < len(lines_s):
    if lines_s[i] in translation:
        sys.stdout.write(translation[lines_s[i]])
    else:
        sys.stdout.write(lines_s[i])
    i += 1