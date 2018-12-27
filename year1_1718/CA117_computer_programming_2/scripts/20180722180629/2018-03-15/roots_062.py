#!/usr/bin/env python3

import sys
from math import sqrt

def discr(a, b, c):
    """Return the quadratic discriminant"""
    return b**2 - 4*a*c

def get_quadratic_roots(a, b, c):
    """Get roots of a quadratic given its coefficients. Handles real and complex roots. Roots returned as a tuple, even if they are the same."""
    dis = discr(a, b, c)
    if 0 <= dis:
        x_p = (-b+sqrt(dis)) / (2*a)
        x_n = (-b-sqrt(dis)) / (2*a)
    else:
        x_p = (-b+sqrt(abs(dis))*1j) / (2*a)
        x_n = (-b-sqrt(abs(dis))*1j) / (2*a)
    return (x_p, x_n)

def main():
    for line in sys.stdin:
        a, b, c = [int(coeff) for coeff in line.strip().split()]
        
        if 0 <= discr(a, b, c):
            r1, r2 = get_quadratic_roots(a,b,c)
            print('r1 = {}, r2 = {}'.format(r1, r2))
        else:
            print(None)

if __name__ == '__main__':
    main()