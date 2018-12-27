#!/usr/bin/env python3

def power(m, n):
    # Return m to the power of n
    # m**n = m*m*m*m*...*m (n times)

    # The simplest case
    if n == 0:
        return 1

    # Case to be decomposed
    return m * power(m, n-1)

def main():
    print(power(5,0))
    print(power(3,1))
    print(power(2,3))
    print(power(4,4))
    print(power(2,32))
    print(power(10,3))
    print(power(8,0))
    print(power(100, 996))
    try:
        print(power(323, 997))
    except RuntimeError:
        print('arguments are too large')

if __name__ == '__main__':
    main()