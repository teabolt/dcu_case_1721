#!/usr/bin/env python3

def get_frequency(iterable):
    """Return a dictionary representing the number of occurrences(value) of an iterable's element(key)."""
    f = {}
    for i in iterable:
        if i not in f:
            f[i] = 1
        else:
            f[i] += 1
    return f

def swap_unique_keys_values(d):
    swapped_d = {}
    frequency = get_frequency(d.values())
    for (k, v) in d.items():
        if frequency[v] != 1:
            continue
        swapped_d[v] = k
    return swapped_d

def main():
    my_dict = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
    print(swap_unique_keys_values(my_dict))
    d = {32:'s', 400:'s'}
    print(swap_unique_keys_values(d))

if __name__ == '__main__':
    main()