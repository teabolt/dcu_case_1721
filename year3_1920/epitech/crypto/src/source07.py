#!/usr/bin/env python3

import sys
import base64
from Crypto.Cipher import AES
from hex_to_base64 import (
    hex_to_byteslike,
    hex_to_unicode,
    base64_to_byteslike,
    byteslike_to_base64,
)
from utils import get_groups
from aes_encryption import (
    ecb_decrypt,
    pcks7_pad,
    pcks7_unpad,
    manual_unpad,
)


def main():
    if len(sys.argv) != 2:
        print("""Usage:
              program filename

              filename - file whose contents will be transformed.
              """)
        sys.exit(84)
    file = sys.argv[1]
    try:
        with open(file) as f:
            key = f.readline()
            if key == '':
                sys.exit(84)
            key = key.strip()
            ciphertext = f.readline()
            if ciphertext == '':
                sys.exit(84)
            ciphertext = ciphertext.strip()
    except:
        sys.exit(84)

    try:
        key = hex_to_byteslike(key)
        ciphertext = base64_to_byteslike(ciphertext)
    except:
        sys.exit(84)
    ciphertext, pad_amount = pcks7_pad(ciphertext, len(key))

    plaintext = ecb_decrypt(ciphertext, key)

    plaintext = manual_unpad(plaintext, pad_amount)
    plaintext = pcks7_unpad(plaintext)
    print(byteslike_to_base64(plaintext))


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit(84)