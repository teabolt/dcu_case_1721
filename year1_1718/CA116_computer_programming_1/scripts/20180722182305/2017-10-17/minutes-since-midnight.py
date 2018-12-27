#!/usr/bin/env python

import sys

time = sys.argv[1]

if time[1] == ":":
    s_hour = time[:1]
    s_minute = time[2:]
elif time[2] == ":":
    s_hour = time[:2]
    s_minute = time[3:]

hour = int(s_hour)
minute = int(s_minute)
midnight_minutes = hour*60 + minute

print midnight_minutes