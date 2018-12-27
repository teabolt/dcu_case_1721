#!/usr/bin/env python

n = input()

# 0 to 6 inclusive. 0 = Monday, etc, numbers corresponding to weekdays.

if n == 5 or n == 6:
	print "weekend"
else:
	print "weekday"
