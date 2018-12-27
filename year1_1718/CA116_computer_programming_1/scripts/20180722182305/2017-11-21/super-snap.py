#!/usr/bin/env python

import sys

word_frequency = {}

# combine reading input and linear search loops.
prev_word = sys.stdin.readline().rstrip()
word_frequency[prev_word] = 1
curr_word = sys.stdin.readline().rstrip()
while 0 < len(curr_word) and word_frequency[prev_word] != 2:
    if curr_word not in word_frequency:
        word_frequency[curr_word] = 0
    word_frequency[curr_word] += 1
    prev_word = curr_word
    curr_word = sys.stdin.readline().rstrip()

# if 0 < len(curr_word):
#    print "snap: " + prev_word