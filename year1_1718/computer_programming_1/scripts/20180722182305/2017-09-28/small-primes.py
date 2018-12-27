#!/usr/bin/env python

n = input()

# n < 20

if n == 1:
	print "not prime"
elif (2 < n and n % 2 == 0):
	print "not prime"
elif (n != 3 and n % 3 == 0):
	print "not prime"
elif (n != 5 and n % 5 == 0):
	print "not prime"
else:
	print "prime"

