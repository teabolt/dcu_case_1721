#!/usr/bin/env python3

import sys
from Stack import Stack

def reverse_input(stack):
	for line in sys.stdin:
		stack.push(line.strip())

	while not stack.is_empty():
		print(stack.pop())


def main():
	s = Stack()
	reverse_input(s)


if __name__ == '__main__':
	main()