#!/usr/bin/env python3

import sys

def get_n2t(n):
    """Return a dictionary that maps from numbers(integer strings) to their corresponding text(string), eg: '1' -> 'one'. 
    (TO DO:) This construction is done for numbers from 0 to to the argument 'n'(inclusive)"""
    numtext = {}
    nt_split = []

    zero = {'0':'zero'}
    first_ten = {
    '1':'one',
    '2':'two',
    '3':'three', 
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven', 
    '8':'eight', 
    '9':'nine', 
    }
    ten = {'10':'ten'}
    ten_to_twenty = {
    '11':'eleven',
    '12':'twelve',
    '13':'thirteen',
    '15':'fifteen',
    '18':'eighteen'
    }
    for i in range(14, 20):
        num = str(i)
        first_half = num[-1]
        if num not in ten_to_twenty:
            ten_to_twenty[num] = first_ten[first_half]+'teen'
    tens = {
    '20':'twenty',
    '30':'thirty',
    '40':'forty',
    '50':'fifty',
    '60':'sixty',
    '70':'seventy',
    '80':'eighty',
    '90':'ninety'
    }
    more_tens = {}
    for i in tens:
        for j in first_ten:
            k = int(i)+int(j)
            new_n = tens[i]+'-'+first_ten[j]
            more_tens[str(k)] = new_n
    hundred = {
    '100':'one hundred'
    }

    nt_split = [zero, first_ten, ten, ten_to_twenty, tens, more_tens, hundred]
    for nt in nt_split:
        numtext.update(nt)

    return numtext

def main():
    n2t = get_n2t(100)
    for line in sys.stdin:
        nums = line.rstrip().split()
        text = [n2t[n] for n in nums]
        print(' '.join(text))

if __name__ == '__main__':
    main()