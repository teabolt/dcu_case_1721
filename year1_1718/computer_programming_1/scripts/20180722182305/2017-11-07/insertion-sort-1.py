#!/usr/bin/env python

a = [] # assume reading a list of integers in increasing numerical order

s = raw_input()
while s != "end":
    a.append(int(s)) # assume 's' is an integer
    s = raw_input()

n = input() # assume input() is an integer
a.append(n)

p = len(a) - 1 # loop backwards
while 0 < p and n < a[p-1]: # linear search conditions: p is not negative(worst case last iteration sets it to 0), compare the element to insort with the neighbouring element.
    a[p] = a[p-1] # move the element up
    p = p - 1 # loop counter works backwards

a[p] = n # insert the element in the right position

print p # print the position