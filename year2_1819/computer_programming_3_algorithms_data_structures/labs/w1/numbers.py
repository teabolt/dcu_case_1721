#!/usr/bin/env python3

import sys

def sum_to_k(lst, k):
	n = True
	i = 0
	j = len(lst) - 1
	while n:
		if i == j:
			n = False
		elif lst[i] + lst[j] == k:
			return True
		elif lst[i] + lst[j] < k:
			i += 1
		elif lst[i] + lst[j] > k:
			j -= 1
		

lst = [13]
k = 13
print(sum_to_k(lst, k))