#!/usr/bin/env python3

class Customer(object):
    # Model a customer account

    discount = 0.0

    def __init__(self, name, balance, addr_line1, addr_line2, addr_line3):
        self.name = name
        self.balance = balance # (how much the customer needs to pay)
        self.addr_line1 = addr_line1
        self.addr_line2 = addr_line2
        self.addr_line3 = addr_line3

    def owes(self):
        # Return the amount due by the customer
        return self.balance*(1-self.discount)

    def __str__(self):
        a = []
        a.append(self.name)
        a.append(self.addr_line1)
        a.append(self.addr_line2)
        a.append(self.addr_line3)
        a.append('Balance: {:.2f}'.format(self.balance))
        a.append('Discount: {:d}%'.format(round(self.discount*100)))
        a.append('Amount due: {:.2f}'.format(self.owes()))
        return '\n'.join(a)

class ValuedCustomer(Customer):
    # Model a 'valued' customer

    discount = 0.1

def main():
    c1 = Customer('John', 10032431, '52 Lane House', 'Hollywood', 'USA')
    print(c1)
    c2 = ValuedCustomer('Linda', 100, '34 SpaceX', 'Orbital House', 'Europa')
    print(c2)

if __name__ == '__main__':
    main()