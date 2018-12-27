#! /usr/bin/env python

n = input()

previous = 0
current = 1

i = 0
while i < n:
	print current
	tmp = current
	current = current + previous
	previous = tmp
	i = i + 1