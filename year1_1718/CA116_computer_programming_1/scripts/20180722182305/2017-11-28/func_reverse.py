#!/usr/bin/env python

def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def reverse(a):
    i = 0
    while i < len(a)/2:
        swap(a, i, len(a)-i-1)
        i += 1

def main():
    a = [1, 2, 3, 4, 5, 7, 6, 9, 101203012031]
    print a
    swap(a, 5, 6)
    print a, 5, 6
    swap(a, 0, 4)
    print a, 0, 4
    reverse(a)
    print a

if __name__ == "__main__":
    main()