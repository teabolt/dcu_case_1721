#!/usr/bin/env python

def bsearch(a, q):
    low = 0
    high = len(a)

    while low < high:
        mid = (low+high)/2
        assert low <= mid < high
        
        if a[mid] < q:
            low = mid + 1
            assert a[low-1] < q
        else:
            high = mid
            assert q <= a[high]

    return low

# test cases
assert bsearch([1, 3, 5], 3) == 1 # find position
assert bsearch([3, 3, 5], 3) == 0 # find first position
assert bsearch([43, 64, 7654], 1) == 0 # insert at start
assert bsearch([1, 3, 5, 7, 8], 9) == 5 # insert at end
assert bsearch([2, 3, 5, 6], 4) == 2 # insert at middle