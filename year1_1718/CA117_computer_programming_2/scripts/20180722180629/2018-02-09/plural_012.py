#!/usr/bin/env python3

import sys

vowels = ['a', 'e', 'i', 'o', 'u']
es_endings = ['ch', 'sh', 'x', 's', 'z', 'o']

def pluralize(s):
    if s[-2:] in es_endings or s[-1:] in es_endings:
        return s + "es"
    elif s[-2:-1] not in vowels and s[-1:] == "y":
        return s[:-1] + "ies"
    elif s[-1:] == "f":
        return s[:-1] + "ves" 
    elif s[-2:] == "fe":
        return s[:-2] + "ves"
    else:
        return s + "s"

def main():
    for line in sys.stdin:
        print(pluralize(line.rstrip()))

if __name__ == "__main__":
    main()