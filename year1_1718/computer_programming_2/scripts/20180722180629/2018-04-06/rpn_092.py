#!/usr/bin/env python3

from stack_092 import Stack
from math import sqrt

# Maths operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def negate(a):
    return -a

def root(a):
    return sqrt(a)

# Map operator symbols to operations

binops = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide,
}

uniops = {
    'n':negate,
    'r':root,
}

# RPN calculator

def calculator(line):
    s = Stack()

    # parse the expression
    tokens = line.split()
    for t in tokens:
        if t in binops or t in uniops: # t is an operator
            # algorithm:
            # 1. check if operator is binary/unary
            # 2. get needed number of operands
            # 3. apply operator
            # 4. give back answer
            if t in binops: # t is binary
                # note that operand order is reversed in a stack
                # second operand is popped as first, and first is popped as second
                # because second was read last, and a stack is LIFO
                b = s.pop()
                a = s.pop()
                x = binops[t](a, b)
                s.push(x)
            else: # t is unary
                a = s.pop()
                x = uniops[t](a)
                s.push(x)
        else:
            try: # t is a number
                x = float(t)
                s.push(x)
            except ValueError: # t is something else (invalid)
                raise IndexError

    # final answer
    ans = s.pop()
    if s.is_empty():
        return ans
    else:
        raise IndexError