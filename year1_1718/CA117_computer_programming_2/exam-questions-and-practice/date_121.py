#!/usr/bin/env python3

import random # for testing

class Date(object):
    """Model a date"""

    MONTH_INFO = {
            1: (31, 'January'),
            2: (28, 'February'),
            3: (31, 'March'),
            4: (30, 'April'),
            5: (31, 'May'),
            6: (30, 'June'),
            7: (31, 'July'),
            8: (31, 'August'),
            9: (30, 'September'),
            10: (31, 'October'),
            11: (30, 'November'),
            12: (31, 'December'),
    }

    DAYS_IN_YEAR = 365

    def __init__(self, day, month, year):
        # It is assumed that the supplied argument represents a correct date (eg: no overflows, correct month and day numbers, etc).
        self.day = day
        self.month = month
        self.year = year
        # If the date needs to be normalised, the following won't work:
        # new_date = Date.from_days(date.to_days())
        # instead it is up to the lazy bastard that is the user of this program to code his or her own normalise() function

    def __str__(self):
        return '{:d} {:s} {:d}'.format(self.day, Date.MONTH_INFO[self.month][1], self.year)

    def __gt__(self, other):
        """Return if one date is greater than another"""
        return self.to_days() > other.to_days()

    def to_days(self):
        days = 0

        days += self.day
        for i in range(1, self.month):
            days += Date.MONTH_INFO[i][0]

        days += self.year*Date.DAYS_IN_YEAR

        return days

    @classmethod
    def from_days(cls, days):
        year = 0
        month = 1
        day = 1

        while Date.DAYS_IN_YEAR < days:
            days -= Date.DAYS_IN_YEAR
            year += 1

        while Date.MONTH_INFO[month][0] < days:
            days -= Date.MONTH_INFO[month][0]
            month += 1

        day = days

        return cls(day, month, year)

    def increment_by_N(self, N):
        total_days = self.to_days() + N
        other = Date.from_days(total_days)
        self.day, self.month, self.year = other.day, other.month, other.year

def main():
    d1 = Date(1, 3, 1973)
    d2 = Date(23, 11, 2012)
    print(d1)
    print(d2)

    print(d1.to_days())
    print(d2.to_days())
    d3 = Date(32, 12, 2012)
    d = d3.to_days()
    print(d)
    print(Date.from_days(d))

    # Compare two dates
    assert(d2 > d1)

    # Increment by 1 day
    d2.increment_by_N(1)
    print(d2)

    # Increment by 365 days
    d2.increment_by_N(365)
    print(d2)

    # Increment by 800 days
    d2.increment_by_N(800)
    print(d2)

    # d2.increment_by_N(365+333+31+31+1)
    # print(d2)

    # hardcore tests - randomly generated dates

    # date needing normalisation
    # d4 = Date(50, 13, 0)
    # print(d4)
    # print(from_days(to_days(d4)))

if __name__ == '__main__':
    main()