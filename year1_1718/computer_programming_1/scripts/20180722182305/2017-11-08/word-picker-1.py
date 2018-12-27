#!/usr/bin/env python

words = []
poses = []

s = raw_input()
while s != "end":
    words.append(s)
    s = raw_input()

s = raw_input()
while s != "end":
    poses.append(int(s)) # assume 's' is integer.
    s = raw_input()

i = 0
while i < len(poses):
    print words[poses[i]]
    i += 1