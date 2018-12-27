#!/usr/bin/env python3

import sys

def int_elems(a):
    return [int(x) for x in a]

def get_score(a, b, c):
    return a**2 + b**2 + c**2 + 7*min(a, b, c)

def get_additive_tri_partitions(x):
    """Partition the integer x into three 'summands', eg: some a,b,c such that x = a+b+c(like an integer can be split into factors(multiples)). Return a list of all the possible and allowed partitions."""
    n = 3 # part number.

    partitions = []
    for i in range(0, x+1): # pick the first number, from 0 to x(inclusive), in turn.
        no_1 = i
        for k in range(0, x-no_1+1): # pick the second number, from 0 to x less the first number, in turn.
            no_2 = k
            no_3 = x - no_1 - no_2 # get the last number from the first two.

            assert no_1 + no_2 + no_3 == x
            partitions.append((no_1, no_2, no_3))

    return partitions

def main():
    for line in sys.stdin:
        a, b, c, d = int_elems(line.rstrip().split())
        params = [a, b, c]
        d_partitions = get_additive_tri_partitions(d)

        # partition = (x, y, z)
        #              |  |  | +
        # parametrs = (a, b, c)
        distributions = []
        for d_partition in d_partitions:
            distr = [0]*3
            for i in range(len(distr)):
                distr[i] = params[i] + d_partition[i]
            distributions.append(distr)
        
        scores = []
        for distr in distributions:
            scores.append(get_score(*distr))

        print(max(scores))

if __name__ == '__main__':
    main()