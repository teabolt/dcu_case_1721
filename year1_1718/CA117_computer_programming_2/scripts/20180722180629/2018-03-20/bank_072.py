#!/usr/bin/env python3

class BankAccount(object):
    # Model a bank account

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print('Insufficient funds available')

    def __str__(self):
        return 'Your current balance is: {:.2f} euro'.format(self.balance)

def main():
    b1 = BankAccount()
    print(b1.balance)
    b1.deposit(100)
    print(b1.balance)
    b1.withdraw(100000000000)
    b1.withdraw(100)
    print(b1.balance)
    b2 = BankAccount(332.4193213)
    print(b2)

if __name__ == '__main__':
    main()