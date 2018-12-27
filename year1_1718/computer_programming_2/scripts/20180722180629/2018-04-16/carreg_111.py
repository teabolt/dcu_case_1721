#!/usr/bin/env python3

"""Regex raw string to match car registration numbers, including:
Irish: YYY CC SSSSSS
"""

# string broken over multiple lines with brackets
car = (r'\b\d\d[12]'
    r'\s(?:C|CE|CN|CW|D|DL|G|KE|KK|KY|L|LD|LH|LM|LS|MH|MN|MO|OY|RN|SO|T|W|WH|WX|WW)'
    r'\s[1-9]\d*\b')

# lines 1-3:
# YYY, year, last digit 1 or 2
# CC, county code
# SSSSSS, 1 to 6 digit number, first digit non-zero