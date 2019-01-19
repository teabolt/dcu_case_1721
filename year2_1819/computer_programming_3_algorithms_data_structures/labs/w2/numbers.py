#!/usr/bin/env python3

import sys
import random

def sum_to_k(lst, k):
	i = 0 # start
	j = len(lst) - 1 # end
	while i < j:
		v = lst[i] + lst[j]
		if v < k:
			i += 1 # go up for a bigger value
		elif k < v:
			j -= 1 # go down for a smaller value
		else: # v == k
			print(lst[i], lst[j])
			i += 1

def main():
	n = int(sys.argv[1]) # list length
	lst = [random.randint(1, 20) for x in range(n)]
	k = 13
	lst.sort()
	sum_to_k(lst, k)


if __name__ == '__main__':
	main()