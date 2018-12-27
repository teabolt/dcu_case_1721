#/usr/bin/env python

import os

files = os.listdir(".")

i = 0
while i < len(files):
    if files[i].split(".")[-1] == "py":
        print files[i]
    i += 1