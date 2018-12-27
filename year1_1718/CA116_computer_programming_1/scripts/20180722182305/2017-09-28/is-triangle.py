#!/usr/bin/env python

# Triangle inequality theorem or something from geometry.

a = input()
b = input()
c = input()

if (c<a+b and b<a+c and a<b+c):
	print "yes"
else:
	print "no"