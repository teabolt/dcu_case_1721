#!/usr/bin/env python3

from math import sqrt
import sys

def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    # Return if two circles, defined by (x, y) centres and radius r, overlap.
    d = sqrt((x2-x1)**2 + (y2-y1)**2) # distance between two centres
    return d < r1+r2

def main():
    ns = [int(x) for x in sys.argv[1:]]
    print(overlap(*ns))

if __name__ == '__main__':
    main()