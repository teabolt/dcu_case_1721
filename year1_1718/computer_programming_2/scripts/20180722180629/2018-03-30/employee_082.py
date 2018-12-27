#!/usr/bin/env python3

class Employee(object):
    # Model an employee

    next_employee_number = 0

    def __init__(self, name, hours_worked=0.00, hourly_rate=9.25):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

        self.employee_number = Employee.next_employee_number
        Employee.next_employee_number += 1

    def __str__(self):
        s = []
        s.append('Name: {}'.format(self.name))
        s.append('ID: {:d}'.format(self.employee_number))
        s.append('Hours: {:.2f}'.format(self.hours_worked))
        s.append('Rate: {:.2f}'.format(self.hourly_rate))
        s.append('Wages: {:.2f}'.format(self.hours_worked*self.hourly_rate))
        return '\n'.join(s)

    def add_hours(self, hours):
        self.hours_worked += hours