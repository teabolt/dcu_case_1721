#!/usr/bin/env python3

import sys

def main():
    contacts_d = {}

    details = sys.argv[1]
    with open(details) as details_f:
        for line in details_f:
            contact = line.rstrip().split()
            name, phone, email = contact[0], contact[1], contact[2]
            contacts_d[name] = (phone, email)

    for line in sys.stdin:
        name = line.rstrip()
        print('Name: {}'.format(name))
        try:
            print('Phone: {}'.format(contacts_d[name][0]))
            print('Email: {}'.format(contacts_d[name][1]))
        except KeyError:
            print('No such contact')

if __name__ == '__main__':
    main()