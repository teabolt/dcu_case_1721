#!/usr/bin/env python3

class Student(object):
    """Model a student"""

    def __init__(self, forename, surname, sid):
        self.forename = forename
        self.surname = surname
        self.sid = sid
        self.marks = {}

    def __str__(self):
        s = []
        s.append('Forename: {:s}'.format(self.forename))
        s.append('Surname: {:s}'.format(self.surname))
        s.append('ID: {:d}'.format(self.sid))
        s.append('Average mark: {:.2f}'.format(self.average_mark()))
        return '\n'.join(s)

    def add_mark(self, code, mark):
        """Record per-module (indicated by module code) mark (percentage)"""
        self.marks[code] = mark

    def average_mark(self):
        """Return the average mark of a student,
        calculated as the arithmetic mean of all the marks (module weighings not considered)"""
        total = sum(self.marks.values())
        number = len(self.marks)
        return total/number

def main():
    
    s1 = Student('Boris', 'Spassky', 17345654)
    s2 = Student('Bobby', 'Fischer', 17907321)

    s1.add_mark('CA103', 50)
    s1.add_mark('CA106', 60)
    print(s1)

    s2.add_mark('CA103', 65)
    s2.add_mark('CA106', 66)
    s2.add_mark('CA172', 72)
    print(s2)

if __name__ == '__main__':
    main()
