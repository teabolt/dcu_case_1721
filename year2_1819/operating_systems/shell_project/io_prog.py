import sys
import os

prefix = '[{}]'.format(__file__)
print(prefix, os.listdir())
print(prefix, input('Enter some text'))