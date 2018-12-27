#!/usr/bin/env python3

class Student(object):
    # Model a student

    def __init__(self, surname, forename, sid, modlist=None):
        # default mutable argument value trap occurs 
        # when trying to use 'add_module' after passing nothing to modlist=[]
        if modlist is None:
            modlist = []
        self.surname = surname
        self.forename = forename
        self.sid = sid
        self.modlist = modlist

    def add_module(self, module):
        self.modlist.append(module)

    def del_module(self, module):
        try:
            self.modlist.remove(module)
        except ValueError:
            pass

    def print_details(self):
        print('ID: {}'.format(self.sid))
        print('Surname: {}'.format(self.surname))
        print('Forename: {}'.format(self.forename))
        print('Modules: {}'.format(' '.join(self.modlist)))

def main():
    ### tests broken - change argument order
    s1 = Student(17350000, 'AAAAA', 'Bob', ['CA999'])
    s1.add_module('CA169')
    s1.del_module('CA169')
    print(s1.modlist)
    print(Student.__init__.__defaults__)
    s1.print_details()

    s2 = Student(9999999, 'BBBB', 'John', ['CA000'])
    print(s2.modlist)
    print(Student.__init__.__defaults__)
    s2.print_details()

    s3 = Student(00000000, 'Critical', 'EOR')
    s3.add_module('ERRORHERE?')
    print(s3.modlist)
    print(Student.__init__.__defaults__)
    s3.print_details()

    s4 = Student(10000000, 'Critical2', 'EOR2', [])
    print(s4.modlist)
    print(Student.__init__.__defaults__)
    s4.print_details()

if __name__ == '__main__':
    main()