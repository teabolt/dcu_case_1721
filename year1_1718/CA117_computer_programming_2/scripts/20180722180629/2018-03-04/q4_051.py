#!/usr/bin/env python3

import sys

def mean(a):
    """Return the statistical mean value(arithmetic mean average)(sum divided by number of elements) of the list of integers in 'a'."""
    return sum(a)/len(a)

def mode(a):
    """Return the statistical mode value(most frequent element) of the list of integers in 'a'."""
    return max(a, key=a.count)

def median(a):
    """Return the statistical median(middle value of a sorted data set) of the list of integers 'a'. If there is no middle value, eg: the list length is even, then the median is the average of the two values nearest the centre."""
    a_sorted = sorted(a)
    mid = int(len(a_sorted)/2)
    if len(a_sorted) % 2:
        return a_sorted[mid]
    else:
        return (a_sorted[mid-1]+a_sorted[mid])/2

def main():
    nums = [int(n) for n in sys.stdin]

    stat_measures = [mean, mode, median]
    stat_namings = [s.__name__.capitalize() for s in stat_measures]
    stat_results = [s(nums) for s in stat_measures]

    for (name, result) in zip(stat_namings, stat_results):
        print('{}: {:.1f}'.format(name, result))

if __name__ == '__main__':
    main()