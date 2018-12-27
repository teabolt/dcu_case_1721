#!/usr/bin/env python3

import sys

def main():
    vowels = 'aeiou'
    for line in sys.stdin:
        word = line.rstrip()
        vows = [c for c in word.lower() if c in vowels]
        if ''.join(vows) == vowels:
            print(word)

if __name__ == '__main__':
    main()