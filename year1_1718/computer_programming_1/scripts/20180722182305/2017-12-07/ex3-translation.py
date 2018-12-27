#!/usr/bin/env python

import sys

def translate(words, translation):
    output = []
    i = 0
    while i < len(words):
        word = words[i]
        if word in translation:
            output.append(translation[word])
        else:
            output.append(word)
        i += 1
    return output

translation = {}

with open("translation.txt") as tr_in:
    tr = tr_in.readline().rstrip()
    while 0 < len(tr):
        words = tr.split()
        translation[words[0]] = words[1]
        tr = tr_in.readline().rstrip()

line = sys.stdin.readline()
while 0 < len(line):
    words = line.split()
    output = translate(words, translation)
    print " ".join(output)
    line = sys.stdin.readline()