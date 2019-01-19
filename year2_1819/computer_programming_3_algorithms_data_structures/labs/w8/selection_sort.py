#!/usr/bin/env python3

import sys


""" Selection sort algorithm """
def selection_sort1(lst):
    cmp_count = 0
    mov_count = 0
    for i in range(len(lst) - 1):   # go from 0 to one less the last index
        # Find the smallest item in the lst starting at i
        min_index = i
        for j in range(min_index + 1, len(lst)):    # go from one more than the start of the sublist to the end
            if lst[j] < lst[min_index]:
                min_index = j
            cmp_count += 1  # did a compare in the if condition (regardless if entered/didn't the if body)
        # place smallest at the beginning (swap min index with i)
        lst[i], lst[min_index] = lst[min_index], lst[i]
        mov_count += 3  # a swap is three moves (tmp=lst[i], lst[i]=lst[min_index], lst[min_index]=tmp)
        # a move involves an access of a list in an assignment statement
    return (cmp_count, mov_count)


def selection_sort2(lst):
    cmp_count = 0
    mov_count = 0
    for i in range(len(lst) - 1):
        # Find the smallest item in the lst starting at i
        min_index = i
        for j in range(min_index + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
            cmp_count += 1
        # place smallest at the beginning (swap min index with i)
        if min_index != i:  # no 'comparison' here (doesn't involve access to a list)
            lst[i], lst[min_index] = lst[min_index], lst[i]
            mov_count += 3  # indeed did a swap
    return (cmp_count, mov_count)


def selection_sort3(lst):
    cmp_count = 0
    mov_count = 0
    lo = 0
    hi = len(lst) - 1
    while lo < hi:
        min_index = lo
        max_index = lo
        for j in range(lo + 1, hi + 1):
            if lst[j] < lst[min_index]:
                min_index = j
                cmp_count += 1  # did this compare (true), the rest will be skipped
            elif lst[j] > lst[max_index]: # maybe >= to get stable sort
                max_index = j
                cmp_count += 2  # did this compare (true) + the one before (false)
            else:   # own addition
                cmp_count += 2  # did two compares (both were false)

        if max_index == lo:
            max_index = min_index   # We will be moving lst[lo] to min_index, so update max_index first

        # swap min index with lo ... place smallest at the first
        lst[lo], lst[min_index] = lst[min_index], lst[lo]
        mov_count += 3  # swap for min
        # swap max index with hi ... place largest at the end
        lst[hi], lst[max_index] = lst[max_index], lst[hi]
        mov_count += 3  # swap for max
        lo += 1
        hi -= 1
    return (cmp_count, mov_count)


def test3():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    
    orig = list(items)

    result = selection_sort3(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)



def test2():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    
    orig = list(items)

    result = selection_sort2(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)


def test1():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    
    orig = list(items)

    result = selection_sort1(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)
    assert selection_sort1([1, 2]) == (1, 3)
    assert selection_sort1([2, 1]) == (1, 3)


def main():
    # test1()
    # test2()
    test3()

if __name__ == "__main__":
    main()
