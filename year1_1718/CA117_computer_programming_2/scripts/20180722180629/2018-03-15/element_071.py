#!/usr/bin/env python3

class Element(object):
    # Type to model a chemical element.

    def __init__(self, num, name, sym, boil_p):
        self.number = num
        self.name = name
        self.symbol = sym
        self.boiling_point = boil_p

    def print_details(self):
        print('Number: {}'.format(self.number))
        print('Name: {}'.format(self.name))
        print('Symbol: {}'.format(self.symbol))
        print('Boiling point: {} K'.format(self.boiling_point))

def main():
    # Testing
    e1 = Element(10000, 'Zenithium Legendary Rare Element', 'ZlRe', 10000000000000000000000000000000000000)
    e1.print_details()

if __name__ == '__main__':
    main()