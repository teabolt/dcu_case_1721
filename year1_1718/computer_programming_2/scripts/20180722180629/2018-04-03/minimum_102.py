#!/usr/bin/env python3

def minimum(a):
    # Return the smallest (integer) element of a list
    # [4, 645, 1] -> 1

    # Bacase:
    if len(a) == 1: # singleton list
        return a[0] # minimum of [x] -> x

    # Recase:
    le = a[0:1] # check against the left side singleton
    a = a[1:]
    if minimum(le) < minimum(a):
        return minimum(le)
    else:
        return minimum(a)

def main():
    print(minimum([3]))
    print(minimum([4, 1]))
    print(minimum([6,5,1,3,4]))
    print(minimum([6,5,11,3,4]))
    print(minimum([6,15,11,13,14]))
    print(minimum([6,15,11,13,4]))

if __name__ == '__main__':
    main()