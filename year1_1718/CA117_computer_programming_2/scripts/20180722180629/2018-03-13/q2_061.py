#!/usr/bin/env python3

import sys

def mean(a):
    # Return the average of a list of integers
    return sum(a)/len(a)

def median(a):
    # Return the middle value, or the average of two middle values, of a list of integers.
    # Assume the list is *already sorted* in ascending(lowest to highest) order.
    N = len(a)
    if N % 2:
        # a has odd number of elements
        return a[N//2]
    else:
        return (a[N//2-1]+a[N//2]) / 2

def main():
    nums = [int(n) for n in sys.stdin]
    mu = mean(nums)
    me = median(sorted(nums))
    print('Mean: {:.1f}'.format(mu))
    print('Median: {:.1f}'.format(me))

if __name__ == '__main__':
    main()