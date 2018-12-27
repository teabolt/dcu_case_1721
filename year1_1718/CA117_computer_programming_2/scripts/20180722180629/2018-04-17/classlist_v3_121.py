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

class Classlist(object):
    """Model a collection of students"""

    def __init__(self):
        self.d = {} # mapping from id's to students

    def add(self, stud):
        """Add a student to the classlist"""
        self.d[stud.sid] = stud

    def remove(self, sid):
        """Remove a student from the classlist by id"""
        del(self.d[sid])

    def lookup(self, sid):
        """Look up (return object) a student by id, else return None"""
        if sid in self.d:
            return self.d[sid]
        else:
            return None

    def sort_on(self):
        return self.surname

    def __str__(self):
        s = [str(stud) for stud in sorted(self.d.values(), key=Classlist.sort_on)]
        return '\n'.join(s)

    def max_student(self):
        """Return student with the highest average mark"""
        return max(self.d.values())

    def min_student(self):
        """Return student with the lowest average mark"""
        return min(self.d.values())

def main():
    cl = Classlist()
    s1 = Student('Boris', 'Spassky', 17345654)
    s2 = Student('Bobby', 'Fischer', 17907321)
    s3 = Student('Mikhail', 'Tal', 17884786)

    s1.add_mark('CA103', 50)
    s1.add_mark('CA106', 60)

    s2.add_mark('CA103', 65)
    s2.add_mark('CA106', 66)
    s2.add_mark('CA172', 72)

    s3.add_mark('CA103', 80)
    s3.add_mark('CA106', 90)
    
    cl.add(s1)
    cl.add(s2)
    cl.add(s3)

    print(cl.max_student())
    print(cl.min_student())

if __name__ == '__main__':
    main()