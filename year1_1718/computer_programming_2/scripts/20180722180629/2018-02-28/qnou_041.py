#!/usr/bin/env python3

import sys

def find_all(s, c):
    """Return a list of all the indices that have a character 'c' in the string 's'."""
    indices = []
    i = s.find(c)
    while i != -1:
        indices.append(i)
        i = s.find(c, i+1)
    return indices

def qnou(s):
    """Return True if string s contains *a* 'q' that is not followed by a 'u', otherwise False."""
    all_q = find_all(s, 'q')
    for i in all_q:
        if i == len(s)-1:
            return True
        elif s[i+1] != 'u':
            return True
    return False

def main():
    words = [w.rstrip() for w in sys.stdin]
    words_qnou = [w for w in words if qnou(w.casefold())]
    print('Words with q but no u: {}'.format(words_qnou))

if __name__ == '__main__':
    main()