#!/usr/bin/env python3

import sys

def middle(s):
    return s[len(s) // 2]

def main():
    for line in sys.stdin:
        if len(line.rstrip()) % 2 != 0:
            print(middle(line.rstrip()))
        else:
            print("No middle character!")

if __name__ == "__main__":
    main()