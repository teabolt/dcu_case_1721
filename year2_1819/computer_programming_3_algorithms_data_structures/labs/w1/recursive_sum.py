#!/usr/bin/env python3


import sys


def sumto(a, b):
	# base
	if b <= a:
		return 0

	# recurrence
	assert a < b
	return sumto(a, b-1) + (b-1)


def main():
	a, b = sys.argv[1:]
	print(sumto(int(a), int(b)))


if __name__ == '__main__':
	main()