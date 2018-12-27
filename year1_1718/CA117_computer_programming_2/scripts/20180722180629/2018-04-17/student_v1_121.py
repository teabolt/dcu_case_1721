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

def main():
    s1 = Student('Boris', 'Spassky', 17345654)
    s2 = Student('Bobby', 'Fischer', 17907321)

    assert(s1.forename == 'Boris')
    assert(s1.surname == 'Spassky')
    assert(s1.sid == 17345654)
    
    print(s1)
    print(s2)

if __name__ == '__main__':
    main()