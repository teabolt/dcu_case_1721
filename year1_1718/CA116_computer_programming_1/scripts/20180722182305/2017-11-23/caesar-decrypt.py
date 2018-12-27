#!/usr/bin/env python

import sys

alpha1 = "abcdefghijklmnopqrstuvwxyz"
alpha2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_part = [alpha1, alpha2]
translation = {}
r = -13 # left shift(decrypt); rotation number.

# Get translation.
i = 0
while i < len(alpha_part):
    j = 0
    while j < len(alpha_part[i]):
        translation[alpha_part[i][j]] = alpha_part[i][(j+r)%26]
        j += 1
    i += 1

lines_s = sys.stdin.read()

i = 0
while i < len(lines_s):
    if lines_s[i] in translation:
        sys.stdout.write(translation[lines_s[i]])
    else:
        sys.stdout.write(lines_s[i])
    i += 1