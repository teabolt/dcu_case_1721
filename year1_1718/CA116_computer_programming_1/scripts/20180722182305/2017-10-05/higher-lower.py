#! /usr/bin/env python

prev = input()

i = 0
while i < 5:
	curr = input()
	if prev < curr:
		print "higher"
	elif curr < prev:
		print "lower"
	elif prev == curr:
		print "equal"
	prev = curr
	i = i + 1

