#!/usr/bin/env python3

import random
import sys
import time
import multiprocessing as mp


sys.setrecursionlimit(sys.getrecursionlimit()*sys.getrecursionlimit())


def partition(lst, lo, hi):
    # print('Partitioning by {}'.format(mp.current_process().name))
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


def rec_qsort(lst, lo, hi, subprocess_no, max_subprocesses):
    if lo < hi:
        # print('Sorting by {}'.format(mp.current_process().name))
        pivot = partition(lst, lo, hi)
        # print(pivot)
        if subprocess_no < max_subprocesses:
            subprocesses = subprocess_no + 2
            mp.Process(target=rec_qsort, args=(lst, lo, pivot - 1, subprocesses, max_subprocesses)).start()
            mp.Process(target=rec_qsort, args=(lst, pivot + 1, hi, subprocesses, max_subprocesses)).start()
        else:
            rec_qsort(lst, lo, pivot - 1, subprocess_no, max_subprocesses)
            rec_qsort(lst, pivot + 1, hi, subprocess_no, max_subprocesses)
    # print('Parent done')


def qsort(lst):
    rec_qsort(lst, 0, len(lst)-1, 0, 2)
    # pivot = partition(lst, 0, len(lst)-1)
    # pivot1 = partition(lst, 0, pivot - 1)
    # pivot2 = partition(lst, pivot + 1, len(lst)-1)
    # mp.Process(target=rec_qsort, args=(lst, 0, pivot1 - 1)).start()
    # mp.Process(target=rec_qsort, args=(lst, pivot1 + 1, pivot - 1)).start()
    # mp.Process(target=rec_qsort, args=(lst, pivot + 1, pivot2 - 1)).start()
    # mp.Process(target=rec_qsort, args=(lst, pivot2 + 1, len(lst)-1)).start()


if __name__ == '__main__':
    N = int(sys.argv[1])
    a = [random.randint(-100, 100) for _ in range(N)]
    t1 = time.time()
    qsort(a)
    t2 = time.time()
    print(t2-t1)