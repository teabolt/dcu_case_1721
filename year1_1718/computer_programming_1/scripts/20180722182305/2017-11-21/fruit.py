#!/usr/bin/env python

import sys

fruit = {
   "apple": True,
   "pair": True,
   "orange": True,
   "banana": True,
   "cherry": True,
}

word = sys.stdin.readline().rstrip()
while 0 < len(word):
    if word in fruit:
        print word
    word = sys.stdin.readline().rstrip()