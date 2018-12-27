#! /usr/bin/env python

prev = input()

while prev != 0:
	curr = input()
	if curr == 0:
		prev = curr
	elif prev < curr:
		print "higher"
	elif curr < prev:
		print "lower"
	elif prev == curr:
		print "equal"
	prev = curr
