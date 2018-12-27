#!/usr/bin/env python3

import sys

def is_evil(s):
    for c in 'evil':
        if s.count(c) != 1:
            return False
    evil_at = [s.index(c) for c in 'evil']
    if evil_at == sorted(evil_at):
        return True

def main():
    for line in sys.stdin:
        word = line.rstrip()
        if is_evil(word.casefold()):
            print(word)

if __name__ == '__main__':
    main()