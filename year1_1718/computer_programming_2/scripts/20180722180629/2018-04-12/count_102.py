#!/usr/bin/env python3

def count_letters(s):
    """
    s --> number of characters in s
    Recursive 'len' implementation
    """

    # e-quintuple-Z case:
    if len(s) == 1: # ***THIS IS NOT CHEATING***
        return 1
    elif s == '': # empty string case
        return 0

    # the mind boggling case:
    # count the string componentially
    # backtrack to the base case
    # callback by counting incrementally in 1's
    return count_letters(s[:1]) + count_letters(s[1:])

def main():
    print(count_letters('a'))
    print(count_letters('2'))
    print(count_letters('bc'))

    print(count_letters('cat'))
    print(count_letters('catastrophe'))
    print(count_letters(''))

if __name__ == '__main__':
    main()