#!/usr/bin/env python3

class Student(object):
    """Model a student"""

    def __init__(self, forename, surname, sid):
        self.forename = forename
        self.surname = surname
        self.sid = sid

    def __str__(self):
        s = []
        s.append('Forename: {}'.format(self.forename))
        s.append('Surname: {}'.format(self.surname))
        s.append('ID: {}'.format(self.sid))
        return '\n'.join(s)

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

def main():
    cl = Classlist()
    s1 = Student('Boris', 'Spassky', 17345654)
    s2 = Student('Bobby', 'Fischer', 17907321)

    cl.add(s1)
    cl.add(s2)
    print(cl.d)

    s = cl.lookup(17345654)
    assert(isinstance(s, Student))
    assert(s.forename == 'Boris')
    assert(s.surname == 'Spassky')
    assert(s.sid == 17345654)
    
    cl.remove(17345654)
    print(cl.d)
    s = cl.lookup(17345654)
    assert(s is None)

if __name__ == '__main__':
    main()