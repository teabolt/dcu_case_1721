#!/usr/bin/env python

import os

files = os.listdir(".")

i = 0
while i < len(files):
    file_dir = files[i].split(".")
    if file_dir[-1] == "py":
        with open(".".join(file_dir)) as file:
            if file.read() != "":
                print files[i]
    i += 1