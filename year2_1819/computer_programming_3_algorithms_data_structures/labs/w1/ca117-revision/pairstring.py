#!/usr/bin/env python3


import sys


def main():
    assert 1 < len(sys.argv)
    s = sys.argv[1]
    assert 1 < len(s)

    n = int(sys.argv[2])
    s *= n

    i = 1
    while i < len(s):
        print(s[i-1], s[i], sep='')
        i += 1

    # initialise i = 1 OR change condition to i < len(s) - 1


if __name__ == '__main__':
    main()


# Complexity
# O(n^2) - access elements of string twice (one each, then *one*(!) for each - gets costy over length, but a bit less than O(n^2) in practice?)
# depends on string length
# (even though one loop!?)
# solve with caching of already read values???