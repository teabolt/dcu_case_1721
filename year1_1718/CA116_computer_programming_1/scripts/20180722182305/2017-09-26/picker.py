#!/usr/bin/env python

a = input()
b = input()
c = input()

even = c % 2

print (b * even) + (a * int(not bool(even)))