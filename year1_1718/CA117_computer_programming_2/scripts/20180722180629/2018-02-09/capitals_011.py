#!/usr/bin/env python3

import sys

def capitalize_ends(s):
    return s[0].capitalize() + s[1:-1] + s[-1].capitalize()

def main():
    for line in sys.stdin:
        if 1 < len(line.rstrip()):
            print(capitalize_ends(line.rstrip()))

if __name__ == "__main__":
    main()