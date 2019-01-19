#!/usr/bin/env python3

import sys


def calc_average(numbers):
    return sum(numbers)/len(numbers) # definition of arithmetic mean average
    # this returns a float


def main():
    n = int(sys.argv[1])
    a = [1, 1, 2]
    a *= n
    print(calc_average(a))


if __name__ == '__main__':
    main()


# Complexity
# O(n). Sum touches each element once. length is O(1) / very fast