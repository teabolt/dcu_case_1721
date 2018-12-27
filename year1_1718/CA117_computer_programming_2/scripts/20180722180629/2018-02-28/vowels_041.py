#!/usr/bin/env python3

import sys

vowels = 'aeiou'

def frequency_sort(t):
    return t[1]

def dict_from_count(s_iterable, s_container):
    """Construct a dictionary that maps each of iterable's elements(characters) to the number of times they occur in a text container(string)."""
    frequency = {}
    for i in s_iterable:
        frequency[i] = s_container.count(i)
    return frequency

def main():
    canon_text = sys.stdin.read().casefold()
    vowel_frequency = dict_from_count(vowels, canon_text)

    max_width = len(str(max(vowel_frequency.values())))
    for (k, v) in sorted(vowel_frequency.items(), key=frequency_sort, reverse=True):
        print('{} : {:{}d}'.format(k, v, max_width))

if __name__ == '__main__':
    main()