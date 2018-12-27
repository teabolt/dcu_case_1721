#!/usr/bin/env python

with open("hello.txt", "w") as f_in:
    f_in.write("Hello world." + "\n") # concatenating newline instead of attaching to string for clarity.