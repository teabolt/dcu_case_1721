#!/usr/bin/env python3

import sys
#import time

def bsearch(a, q):
    low = 0
    high = len(a)
    while low < high:
        mid = (low + high)//2

        if a[mid] < q:
            low = mid + 1
        else:
            high = mid

    return low

def contains(a, q, i):
    return i < len(a) and a[i] == q

def reverse(s):
    return s[::-1]

def with_reverse(a, s):
    srev = reverse(s)
    i = bsearch(a, srev)
    return contains(a, srev, i)

def main():
    #t0 = time.time()

    words = [line.rstrip() for line in sys.stdin]
    words_caseless = [w.casefold() for w in words]
    words_caseless_sorted = sorted(words_caseless)
    w_revs = [w for w in words if 5 <= len(w) and with_reverse(words_caseless_sorted, w.casefold())]
    print(w_revs)

    #t1 = time.time()
    #print(t1 - t0)

if __name__ == '__main__':
    main()