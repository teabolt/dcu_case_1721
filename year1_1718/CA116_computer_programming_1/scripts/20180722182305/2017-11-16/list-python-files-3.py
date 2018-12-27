#!/usr/bin/env python

import os

files = os.listdir(".")

i = 0
while i < len(files):
    if files[i].split(".")[-1] == "py":
        with open(files[i]) as file:
            if file.read() != "":
                print files[i]
    else:
        # this fails if the path name is a directory.
        with open(files[i]) as file:
            s = file.readline()
            if s == "#!/usr/bin/env python" or s == "#!/usr/bin/env python\n" :
                print files[i]
    i += 1