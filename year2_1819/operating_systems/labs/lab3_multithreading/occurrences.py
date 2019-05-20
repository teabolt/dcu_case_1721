#!/usr/bin/env python3

import threading


def occurs_count(s, c):
    return s.count(c)


def char_in_file(path, c):
    with open(path, 'r') as f:
        s = f.read()
    return s.count(c)


def main():
    # print(char_in_file('speeches.txt'))
    print(char_in_file('speeches_short.txt', 'a'))


if __name__ == '__main__':
    main()