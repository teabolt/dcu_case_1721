#!/usr/bin/env python3

import sys
import string

def canonize(s):
    s_canon = ""
    for c in s.casefold():
        if c not in string.punctuation and c.isalnum():
            s_canon += c
    return s_canon

def main():
    tokens = sys.stdin.read().split()
    unique_tokens = set()
    for token in tokens:
        token_canon = canonize(token)
        if token_canon: # 'token_canon' should be a non-empty string.
            unique_tokens.add(token_canon) # adding an element already present has *no effect*
    print(len(unique_tokens))

if __name__ == "__main__":
    main()