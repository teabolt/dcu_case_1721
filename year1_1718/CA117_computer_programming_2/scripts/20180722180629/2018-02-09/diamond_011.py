#!/usr/bin/env python3

import sys

def diamond(n):
    line_no = 2*n - 1
    for line in range(1, line_no+1):
        lead_spaces = abs(n - line)
        total_aster = n - lead_spaces

        print(" "*lead_spaces + "*", end='')
        print(" *"*(total_aster - 1))

def main():
    n = int(sys.argv[1])
    diamond(n)

if __name__ == "__main__":
    main()