#!/usr/bin/env python3

import sys

def chop(s):
    return s[1:-1]

def main():
    for line in sys.stdin:
        chopped_line = chop(line.rstrip())
        if chopped_line: # test if the choppped_line is a non-empty string.
            print(chopped_line)

if __name__ == "__main__":
    main()