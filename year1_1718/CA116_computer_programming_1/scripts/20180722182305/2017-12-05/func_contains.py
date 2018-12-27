#!/usr/bin/env python

import func_bsearch

def contains(a, q):
    func_bsearch.bsearch(a, q)
    return q in a

def main():
    print contains([2, 4, 6, 8, 8, 9], 10)

if __name__ == "__main__":
    main()