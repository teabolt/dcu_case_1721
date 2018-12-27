#! /usr/bin/env python

sum_result = 0

n = input()

while n != 0:
	if n < 0:	# absolute value if branch.
		n = -n
	sum_result = sum_result + n
	n = input()

print sum_result

