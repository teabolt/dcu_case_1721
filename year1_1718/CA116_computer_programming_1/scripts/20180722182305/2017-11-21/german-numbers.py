#!/usr/bin/env python

import sys

number_translation = {
    'one': 'eins',
    'two': 'zwei', 
    'three': 'drei', 
    'four': 'vier', 
    'five': 'funf', 
    'six': 'sechs', 
    'seven': 'sieben', 
    'eight': 'acht', 
    'nine': 'neun', 
    'ten': 'zehn', 
}

en_number = sys.stdin.readline().rstrip()
while 0 < len(en_number):
    print number_translation[en_number]
    en_number = sys.stdin.readline().rstrip()