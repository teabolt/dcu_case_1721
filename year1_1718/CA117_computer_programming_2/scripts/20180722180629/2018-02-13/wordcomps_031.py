#!/usr/bin/env python3

import sys

vowels = 'aeiou'

def allvowels(s):
    for v in vowels:
        if v not in s.casefold():
            return False
    return True

def isanagram(word1, word2):
    for c in word1:
        if c in word2:
            word2 = word2.replace(c, '', 1)
        else:
            return False
    return not word2

def count_max(c, word_list):
    c_max = 0
    for word in word_list:
        c_count = word.count(c)
        if c_max < c_count:
            c_max = c_count
    return c_max

def find_by_count(c, n, word_list):
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
    result_list.append(find_by_count('e', count_max('e', words), words))
    return result_list

def main():
    words = []
    for line in sys.stdin:
        words.append(line.rstrip())
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