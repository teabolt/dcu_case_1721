#!/usr/bin/env python3

def reverse_list(a):
    """
    a --> new reversed list
    reverse recursively
    """

    # Initial term
    if len(a) == 0: # empty list []
        return a

    # General recurrence relation
    e = a[0]
    a = a[1:]
    b = reverse_list(a) + [e]
    return b

def main():
    print(reverse_list([]))
    print(reverse_list([1]))
    print(reverse_list([3, 2]))
    print(reverse_list([4, 3, 1, 5]))
    print(reverse_list([3, 2, 1]))

if __name__ == '__main__':
    main()