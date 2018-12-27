#!/usr/bin/env python3

def sumup(n):
    # Recursively calculate the sum from 0 up to n
    # 1 + 2 + 3 + ... + n
    
    # Base case
    if n == 0:
        return 0

    # Recursive case
    return n + sumup(n-1)

def main():
    print(sumup(0))
    print(sumup(1))
    print(sumup(12))

if __name__ == '__main__':
    main()