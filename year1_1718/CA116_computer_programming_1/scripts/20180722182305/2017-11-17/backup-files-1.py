#!/usr/bin/env python

import os

files = os.listdir(".")
non_backup_files = []


i = 0
while i < len(files):
    if files[i].split(".")[-1] != "bak":
        non_backup_files.append(files[i])
        # an alternative to creating a new list for the non-backup files would be popping *at an index* the backup files in the original 'files' list.
    i += 1

i = 0
while i < len(non_backup_files):
    with open(non_backup_files[i]+".bak", "w") as backup_file, open(non_backup_files[i]) as non_backup_file:
        # can also nest and open the non_backup_file here with another 'with-as' statement.
        backup_file.write(non_backup_file.read())
    i += 1