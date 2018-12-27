#!/usr/bin/env python

import sys
words = sys.stdin.read().split() # don't care about whitespace

def is_end_of_sentence_word(word):
    ch = word[len(word)-1]
    return ch in [".", "!", "?"]

i = 0
while i < len(words):
    j = i
    while j < len(words) and not is_end_of_sentence_word(words[j]):
        j += 1
    
    j += 1
    print " ".join(words[i:j])

    i = j

