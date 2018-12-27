#!/usr/bin/env python3

import sys
import calendar

poem_lines = [
    'Monday\'s child is fair of face', 
    'Tuesday\'s child is full of grace',
    'Wednesday\'s child is full of woe',
    'Thursday\'s child has far to go',
    'Friday\'s child is loving and giving',
    'Saturday\'s child works hard for a living',
    'Sunday\'s child is fair and wise and good in every way',
    ]

weekdays = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
    ]

def main():
    day = int(sys.argv[1])
    month = int(sys.argv[2])
    year = int(sys.argv[3])
    weekday = calendar.weekday(year, month, day)
    print('You were born on a {} and {}.'.format(weekdays[weekday], poem_lines[weekday]))

if __name__ == '__main__':
    main()