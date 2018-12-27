#!/usr/bin/env python

def bsearch(a, q):
    low = 0
    high = len(a)

    #print q
    #print a, len(a)
    #print low, high

    while low != high:
        mid = (low+high) / 2

        if a[mid] < q:
            low = mid + 1
        else:
            high = mid

        #print q
        #print a, len(a)
        #print low, mid, high

        assert low == 0 or a[low-1] < q
        assert high == len(a) or q <= a[high]

    return low

def main():
    #print "test"
    #print bsearch([2, 5, 7, 8, 9, 10], 8)
    #assert bsearch([2,3,6,6,7,8], 1) == 0
    #assert bsearch([2,3,6,6,7,8], 2) == 0
    #assert bsearch([2,3,6,6,7,8], 4) == 2
    #assert bsearch([2,3,6,6,7,8], 6) == 2
    #assert bsearch([2,3,6,6,7,8], 8) == 5
    #assert bsearch([2,3,6,6,7,8], 9) == 6
    return None

if __name__ == "__main__":
    main()