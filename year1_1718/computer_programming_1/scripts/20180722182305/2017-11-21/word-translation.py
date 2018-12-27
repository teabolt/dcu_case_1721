#!/usr/bin/env python

import sys

translation = {} # will represent/store the translation file with a dictionary. This may be inefficient with large files, but this is compensated by fast dictionary look-up(unlike finding lines in a file).

with open("translation.txt") as f_trans:
    line = f_trans.readline().rstrip()
    while 0 < len(line):
        translation[line.split()[0]] = line.split()[1]
        line = f_trans.readline().rstrip()

word = sys.stdin.readline().rstrip()
while 0 < len(word):
    print translation[word]
    word = sys.stdin.readline().rstrip()