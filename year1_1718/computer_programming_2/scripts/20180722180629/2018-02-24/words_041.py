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

def main():
    s = sys.stdin.read()
    tokens = s.split()

    words = [canonicalize(w) for w in tokens]
    d = frequencies(words)
    d_alphabetically = sorted(d.keys())

    for i in d_alphabetically:
        print('{} : {}'.format(i, d[i]))

if __name__ == '__main__':
    main()