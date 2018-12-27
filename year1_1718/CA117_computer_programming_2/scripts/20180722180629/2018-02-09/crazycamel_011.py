#!/usr/bin/env python3

import sys

def crazily_camelize(line):
    tokens = line.split()
    crazy_camel = []
    for word in tokens:
        crazy_camel.append(word[:-1] + word[-1].capitalize())
    return " ".join(crazy_camel)

def main():
    for line in sys.stdin:
        print(crazily_camelize(line.rstrip()))

if __name__ == "__main__":
    main()