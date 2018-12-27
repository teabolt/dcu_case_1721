#! /usr/bin/env python

n = input()

has_uninvited_divisors = False

i = 2
while (i < n) and (not has_uninvited_divisors):
	if n % i == 0:
		has_uninvited_divisors = True
	i = i + 1

if n == 1:
	print False
else:
	print not has_uninvited_divisors

