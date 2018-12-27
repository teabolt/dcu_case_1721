#!/usr/bin/env python3

import sys

n2s_d = {
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three', 
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven', 
    '8':'eight', 
    '9':'nine', 
    '10':'ten',
}

def main():
    for line in sys.stdin:
        nums = line.rstrip().split()
        text = []
        for num in nums:
            try:
                text.append(n2s_d[num])
            except KeyError:
                text.append('unknown')
        print(' '.join(text))

if __name__ == '__main__':
    main()