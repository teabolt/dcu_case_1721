#!/usr/bin/env python3

import sys

def main():
    lines = []
    len_longest = 0

    for line in sys.stdin:
        lines.append(line)
        if len_longest < len(line):
            len_longest = len(line)

    for line in lines:
        print("{:^{}}".format(line.rstrip(), len_longest - 1))

if __name__ == "__main__":
    main()