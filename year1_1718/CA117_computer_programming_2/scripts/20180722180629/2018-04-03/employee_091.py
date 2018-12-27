#!/usr/bin/env python3

class Employee(object):
    # Model an employee
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        b = []
        b.append('Name: {}'.format(self.name))
        b.append('Number: {}'.format(self.number))
        b.append('Wages: {:.2f}'.format(self.wages()))
        return '\n'.join(b)

    def wages(self):
        return 0.00

class Manager(Employee):
    # Model a manager employee
    
    def __init__(self, name, number, salary):
        super().__init__(name, number)
        self.salary = salary

    def wages(self):
        return self.salary / 52

class AssemblyWorker(Employee):
    # Model an assembly worker employee
    
    def __init__(self, name, number, hourly_rate, hours):
        super().__init__(name, number)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def wages(self):
        return self.hours * self.hourly_rate

def main():
    e1 = Manager('Marian', 0, 1000000000000)
    e2 = AssemblyWorker('Freddy', 1, 0.05, 157)
    e3 = Employee('Shaean', 132131)

    print(e1, e2, e3, sep='\n')

    e1 = Manager('Mary', 1, 50000)
    e2 = AssemblyWorker('Fred', 2, 15.50, 40)
    e3 = Employee('Sean', 3)

    print(e1)
    print(e2)
    print(e3)

if __name__ == '__main__':
    main()