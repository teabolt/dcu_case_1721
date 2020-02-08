#!/usr/bin/env python3

from byte_xor_encryption import brute_force as brute_force_single_byte
from byte_xor_encryption import find_message_score
from hex_to_base64 import (
    hex_to_unicode,
    hex_to_byteslike,
    byteslike_to_hex,
    byteslike_to_unicode,
    unicode_to_hex,
)
from utils import get_groups


def encrypt(text, key):
    key = repeat_key(key, len(text))
    xor = int(text, base=16) ^ int(key, base=16)
    return format(xor, '0{}X'.format(len(text)))


def decrypt(ciphertext, key):
    return encrypt(ciphertext, key)


def brute_force(ciphertext):
    # minsize = 5 * 2
    # maxsize = 41 * 2
    # keysizes = list(range(minsize, maxsize))
    # top = sorted(keysizes, reverse=False, key=lambda keysize: find_hamming(keysize, ciphertext))
    # print(top)
    keys = []
    # for keysize in top[:3]:
    for keysize in [32]:
        # print(keysize)
        key = brute_force_key(ciphertext, keysize)
        # print(key)
        keys.append(key)
        # print()

    top_key = sorted(keys, reverse=True, key=lambda key: find_message_score(ciphertext, key))[0]
    # top_key = "523163683452642035373431316D344E"
    # print(len(top_key))
    return top_key


def brute_force_key(ciphertext, keysize):
    """Brute force a key knowing its keysize."""
    # print(list(get_groups(ciphertext, keysize)))
    # b = [byteslike_to_unicode(block) for block in list(get_groups(hex_to_byteslike(ciphertext), keysize))[:-1]]
    # print(unicode_to_hex(transpose_other(b)))
    # print(transpose(ciphertext, keysize))
    # a = '1C5E144855721645565E44541104476E33110F07407208495E521450110E5B23'
    # print(transpose(a, keysize))

    # needed_key = '523163683452642035373431316D344E'
    # full_needed_key = repeat_key(needed_key, len(ciphertext))
    # print(full_needed_key)
    # block = ''.join([ciphertext[i:i+2] for i in range(0, len(ciphertext), keysize)])
    # print(block)
    # print(brute_force_single_byte(block))
    # print()

    transposed = transpose(ciphertext, keysize)
    # print(transposed)

    # transposed = [[ciphertext[i:i+1] for i in range(0, len(ciphertext), keysize)]]

    key = []
    for block in transposed:
        key_character = brute_force_single_byte(block)
        # print(key_character, hex_to_unicode(key_character))
        key.append(key_character)
    return ''.join(key)


def repeat_key(key, message_length):
    key_length = len(key)
    full = message_length // key_length
    partial = message_length % key_length
    return key*full + key[:partial]


# # NOT MINE
# def transpose_other( blocks ):
#     transposed = []
#     block_size = len(blocks[0])
#     num_blocks = len(blocks)
#     for i in range(block_size):
#         tmp = [] 
#         for j in range(num_blocks):
#             # tmp is composed of the i-th character of every block
#             tmp.append( blocks[j][i] )
#         transposed.append( ''.join(tmp) )  
#     return transposed


def transpose(text, size):
    """Return transposed text by size blocks."""
    # transpose by BYTES (2 hex digits)
    blocks = list(get_groups(text, size))
    blocks = blocks[:-1]  # ignore possibly different length block
    # print(blocks)

    transposed_number = size // 2
    # print(transposed_number)
    transposed = [[] for i in range(size//2)]

    for i in range(len(transposed)):
        for j in range(len(blocks)):
            # TODO: optimization
            # print(blocks[j])
            characters = list(get_groups(blocks[j], 2))
            element = characters[i]
            transposed[i].append(element)
        transposed[i] = ''.join(transposed[i])
    # print(transposed)
    return transposed

    # groups = [[] for i in range(length)]
    # for i in range(0, len(text), 2):
    #     groups[i%length].append(text[i:i+2])

    # b = []
    # for group in groups:
    #     b.append(''.join(group))
    # return b


def find_hamming(keysize, ciphertext):
    blocks = get_groups(ciphertext, length=keysize)
    blocks = (next(blocks), next(blocks), next(blocks), next(blocks))
    hamming = find_average_distance(blocks) / keysize
    return hamming


def find_average_distance(blocks):
    # bit_length = len(blocks[0]) * 4
    distances = []
    # for each block, check all the blocks after it
    for i in range(len(blocks)-1):
        for j in range(i+1, len(blocks)):
            # block1 = format(int(blocks[i], base=16), '0{}b'.format(bit_length))
            # block2 = format(int(blocks[j], base=16), '0{}b'.format(bit_length))
            block1 = blocks[i]
            block2 = blocks[j]
            distances.append(hamming_distance(block1, block2))
    return sum(distances) / len(distances)


def hamming_distance(x, y):
    """x and y are hex strings."""
    # if len(x) != len(y):
    #     raise ValueError('hamming distance arguments must have the same length.')
    # distance = 0
    # for bit_x, bit_y in zip(x, y):
    #     if bit_x != bit_y:
    #         distance += 1
    # return distance
    xor = int(x, base=16) ^ int(y, base=16)
    distance = bin(xor).count('1')
    return distance