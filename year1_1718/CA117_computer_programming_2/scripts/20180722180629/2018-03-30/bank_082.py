#!/usr/bin/env python3

class BankAccount(object):

    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, surname, forename, balance=0.00):
        self.surname = surname
        self.forename = forename
        self.balance = balance

        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def __str__(self):
        a = []
        a.append('Name: {} {}'.format(self.surname, self.forename))
        a.append('Account number: {:d}'.format(self.account_number))
        a.append('Balance: {:.2f}'.format(self.balance))
        return '\n'.join(a)

    def __iadd__(self, other):
        self.balance += other
        BankAccount.total_lodgements += 1
        return self

    def lodge(self, amount):
        self.balance += amount
        BankAccount.total_lodgements += 1

    def apply_interest(self):
        self.balance = self.balance + self.balance*BankAccount.interest_rate