#!/usr/bin/env python3

import sys

def get_numtext(n):
    """Return a dictionary mapping numbers(integer string) to their corresponding text(string), eg: '1' -> 'one'. 
    (TO DO:) This construction is done for numbers from 0 to to the argument 'n'(inclusive)"""
    numtext = {}
    texts = []
    # Unique(handmade) mappings
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
        new_n = first_ten[num[-1]]+'teen'
        if num not in ten_to_twenty:
            ten_to_twenty[num] = new_n  
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
            more_tens[k] = new_n
    hundred = {
    '100':'hundred'
    }

    texts = [zero, first_ten, ten, ten_to_twenty, tens, more_tens, hundred]
    for d in texts:
        numtext.update(d)

    return numtext

def main():
    for line in sys.stdin:
        nums = line.rstrip().split()
        ntext = get_numtext(100)
        text = [ntext[n] for n in nums]
        print(' '.join(text))

if __name__ == '__main__':
    main()