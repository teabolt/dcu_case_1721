#!python2

import sys

points = {}

s = sys.stdin.readline()
while 0 < len(s):
    point = s.split()
    points[point[0] + "-" + point[1]] = True
    s = sys.stdin.readline()

print " " + "-"*20

y = 19
while -1 < y:
    sys.stdout.write("|")
    x = 0
    while x < 20:
        if str(x) + "-" + str(y) in points:
            sys.stdout.write("*")
        else:
            sys.stdout.write(" ")
        x += 1
    print "|"
    y -= 1

print " " + "-"*20