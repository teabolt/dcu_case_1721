#!/usr/bin/env python3


import sys


def sum_to_k(lst, k):
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if lst[i] + lst[j] == k:
                (lst[i], lst[j])
            j += 1
        i += 1
# Solution like in the hint. Brute-force made correct.


def main():
    # k = int(sys.argv[1])
    # lst = [int(e) for e in sys.argv[2:]]
    # sum_to_k(lst, k)

    n = int(sys.argv[1])
    lst = [1, 6, 7, 8, 9, 10, 2, 3, 4, 5]
    k = 13
    lst *= n
    sum_to_k(lst, k)


if __name__ == '__main__':
    main()


# Complexity
# O(n^2) - loop twice / look at items twice (asymptotically speaking)