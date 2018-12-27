#!/usr/bin/env python3

import sys
import string

def canonicalize(s):
    """Return a caseless(lowercase) version of s with surrounding punctuation removed."""
    return s.casefold().strip(string.punctuation)

def frequencies(a):
    """Return information on an iterable's element frequency - a dictionary mapping from an element(duplicates ignored) to the number of times that element occured in the iterable."""
    fd = {}
    for i in a:
        if i not in fd:
            fd[i] = 1
        else:
            fd[i] += 1
    return fd

def filtered_dict(d):
    """From a passed dictionary d, return a new dictionary with the items that didn't match certain properties removed."""
    nd = {}
    for i in d:
        if 3 < len(i) and 3 <= d[i]:
            nd[i] = d[i]
    return nd

def main():
    s = sys.stdin.read()
    tokens = s.split()

    words = [canonicalize(w) for w in tokens]
    d = frequencies(words)
    d_main = filtered_dict(d)
    
    max_word_len = len(max(d_main.keys(), key=len))
    snums = [str(n) for n in d_main.values()]
    max_num_len = len(max(snums, key=len))

    for i in sorted(d_main):
        print('{:>{}s} : {:>{}d}'.format(i, max_word_len, d_main[i], max_num_len))

if __name__ == '__main__':
    main()