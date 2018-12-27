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

    def __eq__(self, other):
        """Compare if equal, in terms of average marks"""
        return self.average_mark() == other.average_mark()

    def __lt__(self, other):
        """Compare if less than, in terms of avg. mark"""
        return self.average_mark() < other.average_mark()

def main():    
    s1 = Student('Boris', 'Spassky', 17345654)
    s2 = Student('Bobby', 'Fischer', 17907321)
    s3 = Student('Mikhail', 'Tal', 17884786)

    s1.add_mark('CA103', 50)
    s1.add_mark('CA106', 60)
    print(s1)

    s2.add_mark('CA103', 65)
    s2.add_mark('CA106', 66)
    s2.add_mark('CA172', 72)
    print(s2)

    s3.add_mark('CA103', 60)
    s3.add_mark('CA106', 50)
    print(s3)

    assert(s1 == s3)
    assert(s1 < s2)
    assert(s2 > s3)

if __name__ == '__main__':
    main()
