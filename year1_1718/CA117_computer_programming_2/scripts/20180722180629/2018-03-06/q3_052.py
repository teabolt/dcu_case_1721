#!/usr/bin/env python3

def build_dictionary(filename):
    d = {}
    with open(filename, 'r') as maps_f:
        for line in maps_f:
            k, v = line.rstrip().split()
            d[k] = int(v)
    return d

def extract_range(d, low, high):
    rd = {}
    for (k, v) in d.items():
        if low <= v <= high:
            rd[k] = v
    return rd

def main():
    filename = 'mappings_052.txt'
    d = build_dictionary(filename)
    print(d)
    range_d = extract_range(d, 5, 15)
    print(range_d)

if __name__ == '__main__':
    main()