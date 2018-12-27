#!/usr/bin/env python3

import sys

vowels = 'aeiou'

def allvowels(s):
    for v in vowels:
        if v not in s.casefold():
            return False
    return True

def isanagram(w1, w2):
    return sorted(w1) == sorted(w2) and w1 != w2 # assume a *different* word is required for the words to be  anagramatic.

def biggest_char_count(c, word_list):
    c_max = 0
    for word in word_list:
        c_count = word.count(c)
        if c_max < c_count:
            c_max = c_count
    return c_max

def find_by_char_count(c, n, word_list):
    count_words = []
    for word in word_list:
        if word.count(c) == n:
            count_words.append(word)
    return count_words

def compute_words(words):
    result_list = []

    result_list.append([w for w in words if len(w) == 17])
    result_list.append([w for w in words if 18 <= len(w)])
    v_words = [w for w in words if allvowels(w)]
    result_list.append(min(v_words, key=len))
    result_list.append([w for w in words if w.casefold().count('a') == 4])
    result_list.append([w for w in words if 2 <= w.casefold().count('q')])
    result_list.append([w for w in words if 'cie' in w.casefold()])

    result_list.append([w for w in words if isanagram('angle', w.casefold())])
    
    iary_words = [w for w in words if w.casefold().endswith('iary')]
    result_list.append(len(iary_words))
    result_list.append([w for w in words if 'q' in w.casefold() and 'qu' not in w.casefold()])
    result_list.append(find_by_char_count('e', biggest_char_count('e', words), words))

    return result_list

def main():
    words = [line.rstrip() for line in sys.stdin]
    results = compute_words(words)
    format_s = "\n".join(
        [
        'Words containing 17 letters: {}',
        'Words containing 18+ letters: {}',
        'Shortest word containing all vowels: {}',
        'Words with 4 a\'s: {}',
        'Words with 2+ q\'s: {}',
        'Words containing cie: {}',
        'Anagrams of angle: {}',
        'Words ending in iary: {}',
        'Words with q but no u: {}',
        'Words with most e\'s: {}'
        ])
    print(format_s.format(*results))

if __name__ == '__main__':
    main()