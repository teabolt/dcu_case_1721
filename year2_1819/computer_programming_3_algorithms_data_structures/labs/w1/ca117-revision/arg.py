#!/usr/bin/env python3


import sys


def main():
    # assuming that only need to print the first commandline arg. (not all of them)
    assert 1 < len(sys.argv)
    print(sys.argv[1])


if __name__ == '__main__':
    main()


# Complexity
# O(1), doesn't depend on any variables (just 1 operation)