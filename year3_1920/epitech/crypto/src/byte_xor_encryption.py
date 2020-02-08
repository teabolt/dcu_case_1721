#!/usr/bin/env python3

import math
import collections
from utils import get_groups
from hex_to_base64 import hex_to_unicode


ENGLISH_LETTER_FREQUENCY_ORDER = 'zqxjkvbpygfwmucldrhsnioate'


def decrypt(ciphertext, key):
    key_value = int(key, base=16)
    text_bytes = get_groups(ciphertext, 2)
    plaintext = []
    for byte in text_bytes:
        decrypted = int(byte, base=16) ^ key_value
        decrypted = format(decrypted, 'X')
        plaintext.append(decrypted)
    return ''.join(plaintext)


def encrypt(ciphertext, key):
    return decrypt(ciphertext, key)


def brute_force(ciphertext):
    """Break the ciphertext hex string."""
    possibilities = [(key, hex_to_unicode(decrypt(ciphertext, key))) for key in get_keys()]
    top = sorted(possibilities, reverse=True, key=lambda pos: get_score(pos[1]))
    return top[0][0]


def get_keys(bits=8):
    keys_number = 2**bits
    half_bytes_number = math.ceil(bits / 4)
    for k in range(keys_number):
        yield format(k, '0{}X'.format(half_bytes_number))


def get_letter_frequency(message):
    count = collections.Counter(message)
    return count.most_common()


def get_character_score(symbol, count):
    symbol = symbol.lower()  # normalize
    index = ENGLISH_LETTER_FREQUENCY_ORDER.find(symbol)
    index = index + 1  # 0 will be reserved for 'not found'
    # weight * amount
    return (index+1) * count


def get_score(text):
    # linear combination of scores for each character
    score = 0
    for symbol, count in get_letter_frequency(text):
        score += get_character_score(symbol, count)
    return score


def find_message_score(ciphertext, key):
    message = hex_to_unicode(decrypt(ciphertext, key))
    return get_score(message)