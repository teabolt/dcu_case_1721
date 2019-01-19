#!/usr/bin/env python3

from stack import Stack
import sys


def reverse_lines(stack):
    for line in sys.stdin:
        stack.push(line.strip())

    while not stack.is_empty():
        print(stack.pop())


def main():
    s = Stack()
    reverse_lines(s)


if __name__ == '__main__':
    main()