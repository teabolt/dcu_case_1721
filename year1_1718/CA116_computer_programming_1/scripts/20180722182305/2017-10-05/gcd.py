#! /usr/bin/env python

a = input()
b = input()

# Calculate GCD of a and b. a and b values will be used and changed. The answer will be stored in a.

while b != 0:
	tmp = a
	a = b
	b = tmp % b

print a