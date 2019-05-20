#!/usr/bin/env python3

from time import sleep

prefix = '[{}]'.format(__file__)

# N = int(input(prefix + " Enter amount of seconds to sleep for: "))
N = 5
print(prefix, 'sleeping for {} seconds'.format(N))
sleep(N)
# print(prefix, '**', input("Enter special message: "))
print(prefix, 'finished sleep')