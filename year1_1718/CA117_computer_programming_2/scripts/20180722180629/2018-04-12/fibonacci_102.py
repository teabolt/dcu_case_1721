#!/usr/bin/env python3

def fibonacci(n):
    """Return the nth number of the Fibonacci Sequence. 
    Seeds are assumed to be 0:1, 1:1."""

    # Seed values
    if n == 0:
        return 1
    elif n == 1:
        return 1

    # Generic recurrence relation expression
    return fibonacci(n-2)+fibonacci(n-1)

def main():
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(5))
    print(fibonacci(8))
    for i in range(0, 20):
        print(fibonacci(i))

if __name__ == '__main__':
    main()