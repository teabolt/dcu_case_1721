#! /usr/bin/env python

sum_result = 0

i = 0
while i < 5:
	n = input()
	if n < 0:
		n = -n 
		# get absolute value of a negative number with unary '-'.
	sum_result = sum_result + n # add input to sum total

	i = i + 1

print sum_result