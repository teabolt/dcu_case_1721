#!/usr/bin/env python3

import sys

def is_contained(sub, s):
    for c in sub:
        if c in s:
            s = s.replace(c, "", 1)
        else:
            return False
    return True # having passed the 'for' loop, it's known that all 'sub' characters are contained in 's'

def main():
    for line in sys.stdin:
        tokens = line.rstrip().split()
        sub_s = tokens[0].casefold()
        s = tokens[1].casefold()
        print(is_contained(sub_s, s))

if __name__ == "__main__":
    main()