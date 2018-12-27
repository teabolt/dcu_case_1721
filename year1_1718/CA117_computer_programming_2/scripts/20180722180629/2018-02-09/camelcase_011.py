#!/usr/bin/env python3

import sys

def camelize(line):
    tokens = line.split()
    camel = []
    for word in tokens:
        camel.append(word.capitalize())
    return " ".join(camel)

def main():
    for line in sys.stdin:
        print(camelize(line.rstrip()))

if __name__ == "__main__":
    main()