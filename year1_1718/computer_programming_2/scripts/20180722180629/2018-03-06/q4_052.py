#!/usr/bin/env python3

import sys

def get_calorie_stats(filename):
    """Return a dictionary mapping from foodstuffs(string) to their calorie content(integer), from the lines of a file with name 'filename'."""
    d = {}
    with open(filename, 'r') as calorie_data:
        for line in calorie_data:
            tokens = line.rstrip().split()
            food, calories = ' '.join(tokens[:-1]), int(tokens[-1])
            d[food] = calories
    return d

def dtransform_list(a, d, default):
    """Return a list with each element of list 'a' replaced by values in dictionary 'd'(original elements act as the keys). If the key is not present, assign the 'default' value."""
    new_a = []
    for e in a:
        try:
            new_a.append(d[e])
        except KeyError:
            new_a.append(default)
    return new_a

def get_calories(t):
    return t[1]

def main():
    calorie_table = get_calorie_stats(sys.argv[1])

    peoples_calories = {}
    for line in sys.stdin:
        tokens = line.rstrip().split(',')
        name, consumed_foodstuffs = tokens[0], tokens[1:]
        consumed_calories = dtransform_list(consumed_foodstuffs, calorie_table, 100)
        total_calories = sum(consumed_calories)
        peoples_calories[name] = total_calories

    len_name = len(max(peoples_calories.keys(), key=len))
    len_numb = len(str(max(peoples_calories.values())))
    for (name, calories) in sorted(peoples_calories.items(), key=get_calories):
        print('{:>{}} : {:>{}}'.format(name, len_name, calories, len_numb))

if __name__ == '__main__':
    main()