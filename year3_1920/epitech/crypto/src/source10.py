#!/usr/bin/env python3

import sys
from hex_to_base64 import (
    base64_to_unicode,
    base64_to_byteslike,
    byteslike_to_base64,
)
from aes_encryption import ecb_decrypt, ecb_encrypt


def decrypt_unknown_string():
    pass


def detect_block_size():
    pass


def detect_is_ecb():
    pass


def pad_to_block_size(byteslike, block_size):
    val = block_size - (len(byteslike) % block_size)
    return byteslike + bytearray([val] * val)
    # https://gist.github.com/adoc/8550490


# would use requests library for this
# and maybe python http.server
def server_call(payload):
    secret_key = bytes('--CRYPTOGRAPHY--', encoding='utf-8')
    secret_string = bytes('CURVE', encoding='utf-8')
    plaintext = base64_to_byteslike(payload) + secret_string
    plaintext = pad_to_block_size(plaintext, len(secret_key))
    return byteslike_to_base64(ecb_encrypt(plaintext, secret_key))


def main():
    plaintext = 'RUxMSVBUSUM='
    ciphertext = server_call(plaintext)
    print(ciphertext)
    decrypted = ecb_decrypt(base64_to_byteslike(ciphertext), bytes(secret_key, encoding='utf-8'))
    print(decrypted)


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit(84)


# didn't have time to finish the rest