#!/usr/bin/env python3

import sys

def l2d(f):
    d = {}
    keys = f.readline().rstrip().split()
    values = [int(value) for value in f.readline().rstrip().split()]
    for i in range(len(keys)):
        d[keys[i]] = values[i]
    return d

def main():
    print(l2d(sys.stdin))

if __name__ == '__main__':
    main()