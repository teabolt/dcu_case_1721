#!/usr/bin/env python

import sys

start_time = sys.argv[1]
duration_time = sys.argv[2]
assert type(start_time) == str, "start_time argument 1 is string type"
assert type(duration_time) == str, "duration_time argument 2 is string type"

# Time formats:
# H:MM
#  ^1
# HH:MM
#   ^2

i = 1
while i < 3 and start_time[i] != ":":
    i += 1
assert 1 <= i <= 2, "i is either 1 or 2"

start_mins = int(start_time[:i])*60 + int(start_time[i+1:])
assert type(start_mins) == int, "start_mins is integer type"

i = 1
while i < 3 and duration_time[i] != ":":
    i += 1
assert 1 <= i <= 2, "i is either 1 or 2"

duration_mins = int(duration_time[:i])*60 + int(duration_time[i+1:])
assert type(duration_mins) == int, "duration_mins is integer type"

end_mins = start_mins + duration_mins

if (end_mins / 60) < 24:
    end_time_h = str(end_mins / 60)
    assert int(end_time_h) < 24 and end_mins / 60 < 24, "end_time_h is less than 23 hours just like its no 'clock wrap' counterpart"
else:
    end_time_h = str((end_mins / 60) % 24)
    assert int(end_time_h) < 24 and 23 < end_mins / 60, "end_time_h as integer is less than 24, whereas without the 'clock wrap' restriction it is greater than 23(no wrap)"
assert int(end_time_h) < 24, "end_time_h as integer is less than 24(hours wrap around the 24-hour clock)"

if (end_mins % 60) < 10:
    end_time_m = "0" + str(end_mins % 60)
else:
    end_time_m = str(end_mins % 60)
assert int(end_time_m) < 59, "end_time_m as integer is less than 59(minutes wrap around when they become 60)"

end_time = end_time_h + ":" + end_time_m

print end_time