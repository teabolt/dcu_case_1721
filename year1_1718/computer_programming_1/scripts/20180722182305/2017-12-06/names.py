#!/usr/bin/env python

import sys

names_sexes = {}

with open("boys.txt") as f_boys, open("girls.txt") as f_girls:
    name = f_boys.readline().rstrip()
    while 0 < len(name):
        names_sexes[name] = "boy"
        name = f_boys.readline().rstrip()

    name = f_girls.readline().rstrip()
    while 0 < len(name):
        if name in names_sexes:
            names_sexes[name] = "either"
        else:
            names_sexes[name] = "girl"
        name = f_girls.readline().rstrip()

name = sys.stdin.readline().rstrip()
while 0 < len(name):
    print name, names_sexes[name]
    name = sys.stdin.readline().rstrip()