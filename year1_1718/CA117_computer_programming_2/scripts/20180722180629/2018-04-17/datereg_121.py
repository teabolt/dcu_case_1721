#!/usr/bin/env python3

date = r'\b(?:[1-9]|1\d|2\d|3[01])[-/](?:[1-9]|1[012])[-/]\d{4}\b'

# from re import findall
# import sys

# def main():

#     # Verify regular expression is not overly long
#     assert(len(date) < 70)

#     s = sys.stdin.read()
    
#     datelist = findall(date, s)
#     print('Dates: {}'.format(datelist))

# if __name__ == '__main__':
#     main()