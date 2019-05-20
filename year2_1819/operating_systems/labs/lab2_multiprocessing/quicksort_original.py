#!/usr/bin/env python3

import random
import sys

def partition(lst, lo, hi):
    part = lo
    while lo < hi:
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
        while lst[hi] > lst[part]:
            hi -= 1
        if lo < hi:
            lst[hi], lst[lo] = lst[lo], lst[hi]
    if lst[part] > lst[hi]:
        lst[part], lst[hi] = lst[hi], lst[part]
    return hi


def rec_qsort(lst, lo, hi):
    if lo < hi:
        pivot = partition(lst, lo, hi)
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)


def qsort(lst):
    rec_qsort(lst, 0, len(lst) - 1)


if __name__ == '__main__':
    N = int(sys.argv[1])
    a = [random.randint(-100, 100) for _ in range(N)]
    qsort(a)