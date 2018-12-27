import sys
import calendar

def main():
    poem_lines = [
    'Monday\'s child is fair of face', 
    'Tuesday\'s child is full of grace',
    'Wednesday\'s child is full of woe',
    'Thursday\'s child has far to go',
    'Friday\'s child is loving and giving',
    'Saturday\'s child works hard for a living',
    'Sunday\'s child is fair and wise and good in every way',
    ]

    weekdays = {
    0:"Monday",
    1:"Tuesday",
    2:"Wednesday",
    3:"Thursday",
    4:"Friday",
    5:"Saturday",
    6:"Sunday",
    }

    day = int(sys.argv[1])
    month = int(sys.argv[2])
    year = int(sys.argv[3])
    weekday = calendar.weekday(year, month, day)
    print("You were born on a {} and {}.".format(weekdays[weekday], poem_lines[weekday]))

if __name__ == "__main__":
    main()