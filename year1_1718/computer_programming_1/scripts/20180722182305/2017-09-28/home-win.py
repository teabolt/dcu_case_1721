#!/usr/bin/env python

home = input()
away = input()

# Scores of home and away teams in a football soccer match.
# Just abstract scores, no internal things, that you just compare.

if away < home:
	print "Home win."
elif home == away:
	print "Draw."
elif home < away:
	print "Away win."

# need the dots

