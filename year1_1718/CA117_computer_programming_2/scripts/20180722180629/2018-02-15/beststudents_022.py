#!/usr/bin/env python3

import sys

def get_name(line):
    return ' '.join(line.split()[1:])

def get_mark(line):
    mark_s = line.split()[0]
    try:
        mark = int(line.split()[0])
    except ValueError:
        print('Invalid mark {} encountered. Skipping.'.format(mark_s))
        return -1 # Assume marks are positive integers.
    return mark

def get_students_by_mark(students_list, mark_needed):
    return [get_name(line) for line in students_list if get_mark(line) == mark_needed]

def main():
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as student_marks:
            names_and_marks = [line.rstrip() for line in student_marks]
            best_mark = -1
            for line in names_and_marks:
                mark_s = line.split()[0]
                try:
                    mark = int(line.split()[0])
                except ValueError:
                    print('Invalid mark {} encountered. Skipping.'.format(mark_s))
                    continue
                if best_mark < mark:
                    best_mark = mark
            best_students = ', '.join(get_students_by_mark(names_and_marks, best_mark))
            print('Best student(s): {}'.format(best_students))
            print('Best mark: {}'.format(best_mark))
    except FileNotFoundError:
        print('The file {} could not be opened.'.format(filename))

if __name__ == '__main__':
    main()