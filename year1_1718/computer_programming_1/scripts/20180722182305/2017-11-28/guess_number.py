#!/usr/bin/env python

import secret_number
n = 50

def play():
    p = 500
    i = 0
    while i < n and secret_number.guess(p) != "correct":
        if secret_number.guess(p) == "too-low":
            p += p/2
        else: # 'too-high'
            p -= p/2
        print p
        i += 1

play()