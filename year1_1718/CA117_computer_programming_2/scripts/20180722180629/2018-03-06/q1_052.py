#!/usr/bin/env python3

import sys

def main():
    s = sys.argv[1]
    N = int(sys.argv[2])
    Nm = N % len(s)
    print(s[-Nm:]+s[:-Nm])

if __name__ == '__main__':
    main()