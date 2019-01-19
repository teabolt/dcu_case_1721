#!/usr/bin/env python3


import sys


def above_average(lst):
    avg = sum(lst)/len(lst)
    return [e for e in lst if avg < e]


def main():
    n = int(sys.argv[1])
    a = [1, 2]
    a *= n
    above_average(a)



if __name__ == '__main__':
    main()


# Complexity
# O(n^2) - find average (O(n)), then go through each item of the list again (O(n)) - total two checks on input -> O(n^2)
# Better way? Implement checking while calculating average? Possible?