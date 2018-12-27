#!/usr/bin/env python

home_try = input()
home_con = input()
home_pen = input()
away_try = input()
away_con = input()
away_pen = input()

home_points = (home_try * 5) + (home_con * 2) + (home_pen * 3)
away_points = (away_try * 5) + (away_con * 2) + (away_pen * 3)

if away_points < home_points:
    print "home win"
elif home_points < away_points:
    print "away win"
else:
    print "draw"