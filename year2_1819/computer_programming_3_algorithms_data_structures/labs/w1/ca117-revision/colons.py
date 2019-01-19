#!/usr/bin/env python3


import sys


def main():
    args = sys.argv[1:]
    assert args # there is at least one argument

    # solution 1 - insertion and separation
    print(':{}:'.format(':'.join(args)))
    # this prints just '::' if there are no arguments!


    # # solution 2 - fence-post/head-tail problem
    # print(':', end='') # head ':'
    # for arg in args:
    #     print(arg+':', end='')
    # print() # tail '\n'


    # # solution 3 - hidden args
    # # head
    # args1 = args[:]
    # args1.insert(0, '')
    # for arg in args1:
    #     print(arg+':', end='')
    # print()

    # # tail
    # args2 = args[:]
    # args2.append('')
    # for arg in args2:
    #     print(':'+arg, end='')
    # print()


if __name__ == '__main__':
    main()


# Complexity
# O(n) -> depends on argument length
# Get MemoryError if number of arguments is too large