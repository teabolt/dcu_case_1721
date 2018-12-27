#!/usr/bin/env python3

import sys

def get_mark(line):
    mark_s = line.split()[0]
    try:
        mark = int(line.split()[0])
    except ValueError:
        print('Invalid mark {} encountered. Skipping.'.format(mark_s))
        return -1 # Assume marks are positive integers. 
    return mark
    
def main():
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as student_marks:
            best_stud_with_mark = max([line.rstrip() for line in student_marks], key=get_mark)
            tokens = best_stud_with_mark.split()
            best_stud = ' '.join(tokens[1:])
            try:
                best_mark = int(tokens[0])
            except ValueError:
                exit()
            print('Best student: {}'.format(best_stud))
            print('Best mark: {}'.format(best_mark))
    except FileNotFoundError:
        print('The file {} could not be opened.'.format(filename))
        

if __name__ == '__main__':
    main()