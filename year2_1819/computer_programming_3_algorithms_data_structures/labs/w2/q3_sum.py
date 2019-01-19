#!/usr/bin/env python3

import sys
import random


def sum_list(a):
   sum = 0
   for n in a:
      sum += n
   return sum


def main(n):
	a = [random.randint(-100, 100) for x in range(n)]
	sum_list(a)


if __name__ == '__main__':
	main(int(sys.argv[1]))