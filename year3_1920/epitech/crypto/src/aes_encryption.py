#!/usr/bin/env python3

from Crypto.Cipher import AES

from utils import hex_xor, get_groups, byteslike_xor
from hex_to_base64 import (
    byteslike_to_hex,
    hex_to_base64,
    base64_to_hex,
    hex_to_byteslike,
    base64_to_byteslike,
    byteslike_to_unicode,
    byteslike_to_str,
    join_byteslike,
    byteslike_to_base64,
)


def cbc_decrypt(ciphertext, key, IV):
    """Decrypt ciphertext with the given key and Initialization Vector
       into plaintext"""
    ciphertext = base64_to_byteslike(ciphertext)
    key = hex_to_byteslike(key)
    block_size = len(key)

    # ciphertext has padding - we need to ignore it
    ciphertext = remove_cipher_padding(ciphertext, block_size)

    plaintext = []
    prev = hex_to_byteslike(IV)
    for block in get_groups(ciphertext, block_size):
        # note that we must use the ECB decryption algorithm
        # NOT just regular XOR
        result = ecb_decrypt(block, key)

        # here we can just use regular XOR
        result = byteslike_xor(result, prev)

        plaintext.append(result)
        prev = block

    plaintext = join_byteslike(plaintext)
    return byteslike_to_base64(plaintext)


def ecb_decrypt(ciphertext, key):
    # TODO: optimize this
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)


def ecb_encrypt(ciphertext, key):
    # TODO: optimize this
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(ciphertext)


def pcks7_pad(byteslike, size):
    # see https://gist.github.com/adoc/8550490 for implementation
    value = size - (len(byteslike) % size)
    byteslike = byteslike + bytearray([value] * value)
    return byteslike, value
    # FIXME: get padding even if string is of the multiple length?


def pcks7_unpad(byteslike):
    """Unpad PCKS7 padded bytes."""
    pad = byteslike[-1]
    if not isinstance(pad, int):
        amount = ord(pad)
    else:
        amount = pad
    padding = byteslike[-amount:]
    if all([ch == pad for ch in padding]):
        # valid padding character
        return byteslike[:-amount]
    else:
        # no padding or malformed padding, do nothing
        return byteslike


def manual_unpad(byteslike, amount):
    return byteslike[:-amount]


def remove_cipher_padding(byteslike, size):
    # too many characters
    pad = len(byteslike) % size
    return byteslike[:-pad]