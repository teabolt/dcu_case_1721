#!/usr/bin/env python

import os

files = os.listdir(".")
nb_files = [] # non-backup files

i = 0
while i < len(files):
    if files[i].split(".")[-1] != "bak" and os.path.isfile(files[i]):
        nb_files.append(files[i])
    i += 1

i = 0
while i < len(nb_files):
    with open(nb_files[i]) as nb_file, open(nb_files[i]+".bak", "w") as b_file:
        # 'b_file' backup file opened with write mode(and created if didn't exist before)(overriden if content is already in it).
        b_file.write(nb_file.read())
    i += 1