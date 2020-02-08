#!/usr/bin/env python3

import base64
from utils import get_groups
import sys


def hex_to_base64(hex_text):
    try:
        hex_text = pad_hex(hex_text)
        b = base64.b16decode(hex_text)  # -> bytes
        b64 = base64.b64encode(b)  # -> base64
        b64 = str(b64, encoding='utf-8')  # -> base64 str
        return b64
    except:
        sys.exit(84)

# OR ... a manual version
    # bits = to_bit_string(hex_text)
    # return to_base64(bits)


def pad_hex(hex_text):
    if len(hex_text) % 2 != 0:
        # odd number
        # append a zero to make it even
        # FIXME: not sure if this is what needs to be done?
        hex_text += '0'
    return hex_text


# BASE64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
# BASE64_PAD = '='


# def to_bit_string(hex_bytes):
#     b = []
#     for digit in hex_bytes:
#         # 4, B, ...
#         num = int(digit, base=16)  # B (hex) -> 11 (decimal)
#         bits = format(num, '04b')  # 11 (decimal) -> 1011 (binary)
#         b.append(bits)
#     return ''.join(b)


# def to_base64(bits):
#     b = []
#     for group in get_groups(bits):
#         if len(group) != 6:
#             # pad binary number to reach length 6
#             group = format(group, '0<6')  # 11 -> 110000
#         index = int(group, base=2)  # binary -> decimal
#         digit = BASE64[index]  # decimal index -> base64
#         b.append(digit)
#     b = pad_base64(b)
#     return ''.join(b)


# def pad_base64(digits_list):
#     blocks = list(get_groups(digits_list, length=4))
#     last_block = blocks[-1]  # [A, B, C, D, E, F] -> [E, F]
#     padding_amount = 4 - len(last_block)  # [E, F] -> needs 2 more digits
#     for i in range(padding_amount):
#         digits_list.append(BASE64_PAD)
#     return digits_list


# def base64_to_binary(base64):
#     binary = []
#     for digit in base64:
#         if digit in BASE64:
#             index = BASE64.find(digit)
#             value = format(index, '06b')
#         elif digit in BASE64_PAD:
#             # ignore
#             # FIXME: need to handle discarded least significant zeroes
#             pass
#         else:
#             # raise error...
#             pass
#         binary.append(value)
#     return ''.join(binary)


def base64_to_byteslike(text):
    return base64.b64decode(text)


def base64_to_hex(text):
    return str(base64.b16encode(base64.b64decode(text)), encoding='utf-8')


def base64_to_unicode(text):
    return base64.b64decode(text)


def binary_to_unicode(binary):
    characters = [chr(int(byte, base=2)) for byte in get_groups(binary, 8)]
    return ''.join(characters)


def hex_to_unicode(hex_text):
    characters = [chr(int(byte, base=16)) for byte in get_groups(hex_text, 2)]
    return ''.join(characters)
    # return str(base64.b16decode(hex_text), encoding='utf-8')


def hex_to_byteslike(text):
    return base64.b16decode(text)


def unicode_to_hex(text):
    hex_str = [format(ord(ch), '02X') for ch in text]
    return ''.join(hex_str)


def byteslike_to_hex(byteslike):
    return str(base64.b16encode(byteslike), encoding='utf-8')


def byteslike_to_unicode(byteslike):
    return str(byteslike, encoding='utf-8')


def byteslike_to_str(byteslike):
    return str(byteslike)


def byteslike_to_base64(byteslike):
    return str(base64.b64encode(byteslike), encoding='utf-8')


def join_byteslike(lst):
    concat = b''
    for b in lst:
        concat += b
    return concat


# def bytes_number(base64):
#     # FIXME: handle padding
#     return len(base64) * 6