#!/usr/bin/env python

previous = 0
current = 1

n = input()

while current < n:
	print current
	current = current + previous
	previous = current - previous

