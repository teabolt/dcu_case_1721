#!/usr/bin/env python

import sys

word_count = {}

word = sys.stdin.readline().rstrip()
while 0 < len(word):
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1
    word = sys.stdin.readline().rstrip()

for word in word_count:
    if word_count[word] == 1:
        print word