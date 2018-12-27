#!/usr/bin/env python

n = input()
total = 0

i = 0
while i < n:
    score_type = raw_input()
    if score_type == "try":
        total = total + 5
    elif score_type == "conversion":
        total = total + 2
    elif score_type == "penalty":
        total = total + 3
    i = i + 1

print total