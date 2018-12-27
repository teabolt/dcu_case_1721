#!/usr/bin/env python3

from collections import namedtuple

Student = namedtuple('Student', ['firstname', 'surname', 'id'])
pretty_fields = {'firstname':'First name', 'surname':'Surname', 'id':'ID'} # upon adding more fields, update this.

def show_student(student): # A general solution. For just 3 fields could've instead manually printed.
    for field in student._fields:
        print('{:>10}: {}'.format(pretty_fields[field], getattr(student, field)))

def main():
    # tests
    student1 = Student('John', 'Washington', 12345678)
    show_student(student1)
    student2 = Student('Volkswagen', 'Golf', -10002414510341034012103041)
    show_student(student2)

if __name__ == '__main__':
    main()