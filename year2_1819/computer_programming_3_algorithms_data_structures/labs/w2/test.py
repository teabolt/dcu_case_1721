#!/usr/bin/env python3

import sys
import random


def is_square(n):
   i = 0
   while i * i < n:
      i += 1
   return i * i == n


def main(n):
	# a = [random.randint(-100, 100) for x in range(n)]
	is_square(n)


if __name__ == '__main__':
	main(int(sys.argv[1]))