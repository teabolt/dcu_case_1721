#!/usr/bin/env python3

import sys

def get_dict(filename):
    # Open the supplied file and create a dictionary from the file's lines
    # Each line's format is as follows: 'key value'. key is str, value is int.
    d = {}
    with open(filename, 'r') as f_in:
        for line in f_in:
            c, n = line.strip().split()
            d[c] = int(n)
    return d

def makeable_from(s_to_check, source_s):
    # Return True/False if s_to_check can be made from the letters of source_s
    # Letters can only be used once
    # Not necessarily all of source_s has to be used
    for c in s_to_check:
        if c in source_s:
            # Ensure letters are used only once
            source_s = source_s.replace(c, '', 1)
        else:
            return False
    return True

def get_score(s, d):
    # Return the scrabble score
    total = 0
    for c in s:
        total += d[c]
    return total

def comparer(t):
    # Return the second element of an iterable
    # Useful for min/max/sorted function keys
    return t[1]

def main():
    mapping_filename, word = sys.argv[1:]

    mappings = get_dict(mapping_filename)
    makeable_words = [line.strip() for line in sys.stdin 
    if makeable_from(line.strip(), word)]

    scores = {}
    for w in makeable_words:
        scores[w] = get_score(w, mappings)

    highest = max(scores.items(), key=comparer)
    print('{}: {}'.format(highest[0], highest[1]))

if __name__ == '__main__':
    main()