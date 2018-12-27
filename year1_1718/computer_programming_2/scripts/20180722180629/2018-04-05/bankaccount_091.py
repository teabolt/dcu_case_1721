#!/usr/bin/env python3

class BankAccount(object):
    # Model a bank account    

    next_account_number = 16555232
    account_type = 'General'

    def __init__(self, forename, surname, balance):
        self.forename = forename
        self.surname = surname
        self.balance = balance

        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def __str__(self):
        b = []
        b.append('Name: {} {}'.format(self.forename, self.surname))
        b.append('Account number: {:d}'.format(self.account_number))
        b.append('Account type: {}'.format(self.account_type))
        b.append('Balance: {:.2f}'.format(self.balance))
        return '\n'.join(b)

    def lodge(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Insufficient funds available')
        else:
            self.balance -= amount

class CurrentAccount(BankAccount):
    # Model a current account
    
    overdraft = -1000.00
    account_type = 'Current'

    def __str__(self):
        b = []
        b.append(super().__str__())
        b.append('Overdraft: {:.2f}'.format(self.overdraft))
        return '\n'.join(b)

    def withdraw(self, amount):
        if self.balance - amount < self.overdraft:
            print('Insufficient funds available')
        else:
            self.balance -= amount

class SavingsAccount(BankAccount):
    # Model a savings account
    
    interest_rate = 0.01
    account_type = 'Savings'

    def __str__(self):
        b = []
        b.append(super().__str__())
        b.append('Interest rate: {:.2f}'.format(self.interest_rate))
        return '\n'.join(b)

    def apply_interest(self):
        self.balance += self.balance*self.interest_rate

def main():
    a1 = CurrentAccount('Joe', 'Murphy', 100)
    a2 = SavingsAccount('Mandy', 'Murray', 100)
    a3 = SavingsAccount('Jimmy', 'Smith', 200)
    a4 = BankAccount('Frank', 'Wrigley', 500)

    # Print base classes
    print('Base classes...')
    print(a1.__class__.__bases__)
    print(a2.__class__.__bases__)

    print(BankAccount.next_account_number)

    # Print account details
    print('Account details...')
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print('-' * 20)

    # Call some methods
    a1.lodge(50)
    a1.withdraw(100)
    a1.withdraw(100)
    a1.withdraw(1000)
    a2.withdraw(10)
    a2.withdraw(100)
    a2.lodge(20)
    a2.apply_interest()
    a4.lodge(20)
    a4.withdraw(20)
    a4.withdraw(1000)

    # Some methods should not exist
    try:
        a1.apply_interest()
    except AttributeError:
        print('No such method')
    try:
        a4.apply_interest()
    except AttributeError:
        print('No such method')
    print('-' * 20)

    # Print account details
    print('Account details...')
    print(a1)
    print(a2)
    print(a3)
    print(a4)

if __name__ == '__main__':
    main()