#! /usr/bin/env python

neg_sum = 0
pos_sum = 0

n = input()

while n != 0:
	if n < 0:
		neg_sum = neg_sum + n
	elif 0 < n:
		pos_sum = pos_sum + n
	n = input()

print neg_sum, pos_sum

