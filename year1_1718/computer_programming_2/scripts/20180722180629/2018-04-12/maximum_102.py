#!/usr/bin/env python3

def maximum(a):
    """
    list 'a' -> greatest element (like max(), but recursive)
    assume 'a' is non-empty
    """
    # Base case:
    if len(a) == 1: # singleton list
        return a[0]

    # Recursive case:
    # split the list up and compare, if can't keep on splitting up recursively and trying to compare
    # split to most left part and remaining right part
    # might not be the most efficient solution (eg: middle split better)
    la = a[:1] # warning: do not set a[0], as that gives a list element
    # but we are working with lists, not their elements (numbers)
    ra = a[1:]
    if maximum(la) < maximum(ra): # recursively compare left and right
        return maximum(ra)
    else: # la >= ra
        return maximum(la)
    # in la = ra case, either can be returned

def main():
    print(maximum([2]))
    print(maximum([5, 4]))
    print(maximum([1, 2, -1]))
    max = None # shadow variable. local scope anyways?
    print(maximum([6,5,1,3,4]))
    print(maximum([6,5,11,3,4]))
    print(maximum([6,15,11,13,14]))
    print(maximum([6,15,11,13,4]))
    print(maximum([1, 1, 1, 1, 1]))

if __name__ == '__main__':
    main()