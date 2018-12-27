#!/usr/bin/env python3

class Date(object):
    """Model a date"""

    # access with 'month - 1', where month is the standard 1-12 month number
    months = ['January', 'February', 'March', 'April', 'May', 'June', 
            'July', 'August','September', 'October', 'November', 'December']

    # map from day number to number of days in the month
    # 30, 28, 31
    days_in_month = {
        1: 31,
        2: 28, # February
        3: 31,
        4: 30, # April
        5: 31,
        6: 30, # June
        7: 31,
        8: 31,
        9: 30, # September
        10: 31,
        11: 30, # November
        12: 31,
    }

    def __init__(self, day, month, year):
        """Return new date object with day, month, and year"""
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """Return a date:
        Day(numberic), month(text), year(numeric)"""
        return '{:<d} {:s} {:d}'.format(self.day, Date.months[self.month-1], self.year)

    def __gt__(self, other):
        """Return if one date is greater than another"""
        if self.year > other.year:
            return True
        elif self.month > other.month:
            return True
        else:
            return self.day > other.day

    def increment_by_N(self, N):
        """Increment a day by N days (in-place)"""
        day = self.day + N
        month = self.month
        year = self.year

        while self.days_in_month[self.month-1] < day:
            month += 1
            day -= self.days_in_month[month-1]
            if 12 < month:
                year += 1
                month = 1

        self.day = day
        self.month = month
        self.year = year
        return self

    # def total_days(self):
    #     return self.year*365 + Date.days_in_month[self.month] + self.day

    # @classmethod
    # def from_days(cls, days):
    #     year = days//365
    #     print(year)
    #     month = 1
    #     day = 1
    #     return cls(day, month, year)

def main():
    d1 = Date(1, 3, 1973)
    d2 = Date(23, 11, 2012)
    print(d1)
    print(d2)

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

    d2.increment_by_N(365+333+31+31)
    print(d2)

if __name__ == '__main__':
    main()