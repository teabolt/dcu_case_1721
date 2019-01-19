#!/usr/bin/env python3


import sys


def main():
    assert 1 < len(sys.argv) # have arguments
    s = sys.argv[1]
    N = len(s)
    if N % 2 == 0:
        print(s[N//2:])
    else:
        print(s[0]+s[-1])


if __name__ == '__main__':
    main()


# Complexity
# Increases with string length
# Checks for length are O(1), but slices are O(n^2)?
# Get overflow error if string is too large