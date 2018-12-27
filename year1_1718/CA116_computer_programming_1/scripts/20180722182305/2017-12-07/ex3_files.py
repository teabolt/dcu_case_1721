#!/usr/bin/env python

import sys

def read(filename):
    with open(filename) as f_in:
        s = f_in.read()
    return s

def main():
    print "--------------testing----------------"
    # this depends on test.txt existing
    print read("test.txt")
    sys.stdout.write(read("test.txt")) # no trailing newline

if __name__ == "__main__":
    main()