#/usr/bin/env python3

import sys

def best_student(f_marks_in):
    best_mark = 0
    best_student = ""
    for row in f_marks_in:
        data = row.rstrip().split()
        name = " ".join(data[1:])
        mark = int(data[0])
        if best_mark < mark:
            best_mark = mark
            best_student = name
    return (best_student, best_mark)

def main():
    filename = sys.argv[1]
    try:
        with open(filename) as f_student_marks:
            best = best_student(f_student_marks)
            print("Best student: {}".format(best[0]))
            print("Best mark: {}".format(best[1]))
    except FileNotFoundError:
        print("The file {} could not be opened.".format(filename))

if __name__ == "__main__":
    main()