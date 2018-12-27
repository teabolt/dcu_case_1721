#!/usr/bin/env python

pi = 3.141

def circumference(r):
    return 2*pi*r

def area(r):
    return pi*r**2

def main():
    print circumference(2)
    print area(3)
    print circumference(0)
    print area(0)
    print circumference(-1)
    print area(-3)
    # print circumference("a")
    # print area("b")
    print circumference(1)
    print area(1)

if __name__ == "__main__":
    main()