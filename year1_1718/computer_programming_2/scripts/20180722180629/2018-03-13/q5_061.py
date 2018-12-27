#!/usr/bin/env python3

import sys

def sorter(t):
    return t[1]

def main():
    d = {}
    for line in sys.stdin:
        try:
            team, points = line.strip().split(':')
            total = sum([int(n) for n in points.strip().split()])
            d[team] = total
        except ValueError:
            continue
    
    longest_name = max(d.keys(), key=len)
    largest_score = str(max(d.values()))

    for (k, v) in sorted(d.items(), key=sorter, reverse=True):
        print('{:>{}s}: {:>{}d} points'.format(k, len(longest_name), v, len(largest_score)))

if __name__ == '__main__':
    main()