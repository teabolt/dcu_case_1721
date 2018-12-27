#!/usr/bin/env python3

import sys

def sort_on(t):
    return t[1]

def main():
    d = {}
    skipped = []
    for line in sys.stdin:
        try:
            name, marks = line.strip().split(':')
            marks_list = marks.split(',')
            total_mark = sum([int(m) for m in marks_list])
            d[name] = total_mark
        except ValueError:
            skipped.append(name)
            continue
    
    for (k, v) in sorted(d.items(), key=sort_on, reverse=True):
        print('{} : {}'.format(k, v))
    print('Skipped:')
    for s in skipped:
        print(s)

if __name__ == '__main__':
    main()