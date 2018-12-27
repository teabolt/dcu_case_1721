#!/usr/bin/env python3

import sys

n2s_d = {
    0:'zero',
    1:'one',
    2:'two',
    3:'three', 
    4:'four',
    5:'five',
    6:'six',
    7:'seven', 
    8:'eight', 
    9:'nine', 
    10:'ten',
}

def main():
    for line in sys.stdin:
        n_nums = line.rstrip().split()
        s_nums = []
        for n in n_nums:
            s_nums.append(n2s_d[int(n)])
        print(' '.join(s_nums))

if __name__ == '__main__':
    main()