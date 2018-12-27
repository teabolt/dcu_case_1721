#!/usr/bin/env python3

import sys

#def factors(n):
#    """Return the list of the factors(positive integers exactly dividing n) of n(positive integer).
#    n itself is not included.
#    A list is used as opposed to a set(list iterates faster)."""
#    if n == 1:
#        return []
#
#    assert 1 < n
#    a = [1]
#    i = 2
#    while i < n//2+1:
#        if n % i == 0:
#            a.append(i)
#        i += 1#
#    return a

def sumFac(n):
    """Return the sum of the factors(divisors without remainder) of n(positive integer).
    The factor n(of the number itself) is excluded."""
    factors = [i for i in range(1, n//2+1) if n % i == 0]
    return sum(factors)

def isPerfect(n):
    """Return True/False if n(positive integer) is/is not a perfect number(equal to sum of its factors, itself excluded)."""
    return sumFac(n) == n

def main():
    for line in sys.stdin:
        n = int(line.rstrip())
        print(isPerfect(n))

if __name__ == '__main__':
    main()