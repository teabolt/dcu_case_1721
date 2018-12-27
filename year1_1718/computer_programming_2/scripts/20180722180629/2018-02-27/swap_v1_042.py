#!/usr/bin/env python3

def swap_keys_values(d):
    swapped_d = {}
    for (k, v) in d.items():
        swapped_d[v] = k
    return swapped_d

def main():
    d = {'a':2, 'b':54, 'c':-23}
    print(swap_keys_values(d))

if __name__ == '__main__':
    main()