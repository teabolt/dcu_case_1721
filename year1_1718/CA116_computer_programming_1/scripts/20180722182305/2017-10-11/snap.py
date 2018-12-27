#!/usr/bin/env python

prev = input()
curr = input()

while curr != prev:
    prev = curr
    curr = input()

print "snap", curr