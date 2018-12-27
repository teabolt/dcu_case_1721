#!/usr/bin/env python3

import sys

def replace_3(n):
    if n % 3 == 0:
        return 'X'
    else:
        return n

def isprime(n):
    if n < 2:
        return False
    for d in range(2, n//2+1): # go halfway up to n.
        if n % d == 0:
            return False
    return True

def list_computations(a):
    print("Multiples of 3: {}".format([n for n in a if n % 3 == 0]))
    print("Multiples of 3 squared: {}".format([n**2 for n in a if n % 3 == 0]))
    print("Multiples of 4 doubled: {}".format([n*2 for n in a if n % 4 == 0]))
    print("Multiples of 3 or 4: {}".format([n for n in a if n % 3 == 0 or n % 4 == 0]))
    print("Multiples of 3 and 4: {}".format([n for n in a if n % 3 == 0 and n % 4 == 0]))
    print("Multiples of 3 replaced: {}".format([replace_3(n) for n in a]))
    print("Primes: {}".format([n for n in a if isprime(n)]))

def main():
    N = int(sys.argv[1])
    a = []
    for i in range(1, N+1):
        a.append(i)
    list_computations(a)

if __name__ == '__main__':
    main()