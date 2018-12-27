#!/usr/bin/env python3

import sys

def main():
    path = sys.argv[1]
    phonebook = {}
    with open(path) as contacts:
        for line in contacts:
            contact = line.rstrip().split()
            phonebook[contact[0]] = contact[1]

    for line in sys.stdin:
        name = line.rstrip()
        print('Name: {}'.format(name))
        try:
            print('Phone: {}'.format(phonebook[name]))
        except KeyError:
            print('No such contact')

if __name__ == '__main__':
    main()