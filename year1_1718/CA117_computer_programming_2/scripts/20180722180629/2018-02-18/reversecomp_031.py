#!/usr/bin/env python3

import sys
#import time

def contains_reverse_of(w, a):
    """*Caseless* check on whether a string's reverse is in some list of strings."""
    w_rev = w.casefold()[::-1]
    for s in a:
        if s.casefold() == w_rev:
            return True
    return False

def main():
    #t0 = time.time()
    words = [line.rstrip() for line in sys.stdin]
    ws_with_reverse = [w for w in words if 5 <= len(w) and contains_reverse_of(w, words)]
    print(ws_with_reverse)
    #t1 = time.time()
    #print(t1 - t0)

if __name__ == '__main__':
    main()