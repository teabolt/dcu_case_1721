#!/usr/bin/env python3

import sys

def main():
    for s in sys.stdin:
        upper_s = ''
        for c in s.rstrip():
            if c.isupper():
                upper_s += c
            else:
                upper_s += ' '
        contiguous = upper_s.split()
        print(max(contiguous, key=len))

if __name__ == '__main__':
    main()