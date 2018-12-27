#!/usr/bin/env python3

import sys

def get_mark(line):
    mark_s = line.split()[0]
    try:
        mark = int(line.split()[0])
    except ValueError:
        print('Invalid mark {} encountered. Exiting.'.format(mark_s))
        exit()
    return mark

def main():
    pathname = sys.argv[1]
    try:
        with open(pathname) as student_marks:
            best_student_and_mark = max([line.rstrip() for line in student_marks], key=get_mark)
            tokens = best_student_and_mark.split()
            best_stud = ' '.join(tokens[1:])
            best_mark = tokens[0]
            print('Best student: {}'.format(best_stud))
            print('Best mark: {}'.format(best_mark))
    except FileNotFoundError:
        print('The file {} could not be opened.'.format(pathname))

if __name__ == '__main__':
    main()