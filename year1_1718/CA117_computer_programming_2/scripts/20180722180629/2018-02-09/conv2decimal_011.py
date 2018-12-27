#!/usr/bin/env python3

import sys

def to_base_10(digits, base):
    total = 0
    for i in range(len(digits)):
        total += int(digits[len(digits)-i-1])*base**(i)
    return total

def main():
    for line in sys.stdin:
        tokens = line.rstrip().split()
        num = tokens[0]
        base = int(tokens[1])
        print(to_base_10(num, base))

if __name__ == "__main__":
    main()