#!/usr/bin/env python3

import sys

def main():
    while True:
        line = sys.stdin.readline().rstrip()
        try:
            number = int(line)
            print("Thank you for {}".format(number))
            break
        except ValueError:
            print("{} is not a number".format(line))

if __name__ == '__main__':
    main()