#!/usr/bin/env python3

from re import findall
import sys

date = r'\b(?:\d{1,2}[/-]){2}\d{2}\b'

phone = r'\b01[\s-]\d{7}\b'

email = r'\b\S+@\S+\b'

ldate = r'\b\d+\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d+\b'


def main():
    s = sys.stdin.read()
    print(findall(date, s))
    print(findall(phone, s))
    print(findall(email, s))
    print(findall(ldate, s))

if __name__ == '__main__':
    main()