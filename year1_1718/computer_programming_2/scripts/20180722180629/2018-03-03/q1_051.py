#!/usr/bin/env python3

import sys

def main():
    s = sys.argv[1]
    pairs = []
    for i in range(0, len(s), 2):
        try:
            swapped_pair = s[i+1] + s[i]
        except IndexError:
            swapped_pair = s[i]
        pairs.append(swapped_pair)
    print(''.join(pairs))

if __name__ == '__main__':
    main()