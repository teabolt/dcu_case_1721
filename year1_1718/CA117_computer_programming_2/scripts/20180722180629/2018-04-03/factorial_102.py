#!/usr/bin/env python3

def factorial(n):
    # Recursively calculate the factorial of n (n!)
    # n! = 1 * 2 * ... * (n-1) * n
    
    # Trivial case
    if n == 0:
        return 1 # 0! = 1 (convention)

    # Simplify and backtrack
    return n * factorial(n-1)

def main():
    print(factorial(0))
    print(factorial(1))
    print(factorial(12))
    print(factorial(996))
    try:
        print(factorial(997))
    except RuntimeError:
        print('your n is too big!??')

if __name__ == '__main__':
    main()