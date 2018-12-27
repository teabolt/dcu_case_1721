#!/usr/bin/env python3

import sys

def is_substring(sub, s):
    return sub in s

def main():
    for line in sys.stdin:
        tokens = line.rstrip().split()
        sub_s = tokens[0].casefold()
        s = tokens[1].casefold()
        print(is_substring(sub_s, s))

if __name__ == "__main__":
    main()