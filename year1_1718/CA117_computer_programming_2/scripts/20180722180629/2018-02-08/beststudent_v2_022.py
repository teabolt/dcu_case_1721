#!/usr/bin/env python3

import sys

def best_student(f_marks):
    best_mark = 0
    best_student = ""
    for row in f_marks:
        try:
            tokens = row.rstrip().split()
            mark = int(tokens[0])
            if best_mark < mark:
                best_mark = mark
                best_student = " ".join(tokens[1:])
        except ValueError:
            print("Invalid mark {} encountered. Skipping.".format
                (tokens[0]))
    return best_student, best_mark

def main():
    filename = sys.argv[1]
    with open(filename) as f_student_marks:
        best = best_student(f_student_marks)
        print("Best student: {}".format(best[0]))
        print("Best mark: {}".format(best[1]))

if __name__ == "__main__":
    main()