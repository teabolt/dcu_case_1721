#!/usr/bin/env python3


def rprint(a, b):
    """Recursively print the numbers in range a to b-1,
    each on a new line"""
    
    # base case
    if b - a == 1:
        print(a)
    # recursive case
    elif a < b: 
        rprint(a, b-1)
        print(b-1)


# def rrange(start, stop, step):
#     if stop - start == step: # base case
#         print(start)
#     elif start < stop: # recursive case
#         rrange(start+step, stop, step)
#         print(start)


# charles daly
def main():
    # Read two integers from stdin
    a = int(input())
    b = int(input())
    # a = float(input())
    # b = float(input())
    # Call rprint which should recursively print a..b-1
    rprint(a, b)

if __name__ == "__main__":
    main()