#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        s = line.strip()

        ordered = []
        i = 1
        while i < len(s) and s[i-1] > s[i]:
            i += 1

        j = i+1
        while j < len(s) and s[j-1] <= s[j]:
            j += 1

        #print(s, s[i-1:j])
        ordered.append(s[i-1:j])

        print(max(ordered, key=len))


if __name__ == '__main__':
    main()