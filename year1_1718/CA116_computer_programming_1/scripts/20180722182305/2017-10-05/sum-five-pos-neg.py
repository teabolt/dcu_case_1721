#! /usr/bin/env python

pos_sum = 0
neg_sum = 0

i = 0
while i < 5:
	n = input()
	if n < 0:
		neg_sum = neg_sum + n
	elif 0 < n:
		pos_sum = pos_sum + n
	i = i + 1

print neg_sum, pos_sum