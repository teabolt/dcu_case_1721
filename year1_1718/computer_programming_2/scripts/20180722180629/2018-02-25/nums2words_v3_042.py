#!/usr/bin/env python3

import sys

n2s_d = {
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three', 
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven', 
    '8':'eight', 
    '9':'nine', 
    '10':'ten',    
}

def get_dict(f):
    """Given an open file f, create a dictionary of mappings from it. f contains lines of text, each with two words. The first word will be the key, and the second the value."""
    d = {}
    for line in f:
        word, translation = line.rstrip().split()
        d[word] = translation
    return d

def main():
    path = sys.argv[1]
    with open(path) as translation_f:
        translation = get_dict(translation_f)

    for line in sys.stdin:
        nums = line.rstrip().split()
        text = ' '.join([translation[n2s_d[num]] for num in nums])
        print(text)

if __name__ == '__main__':
    main()