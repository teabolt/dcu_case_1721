#!/usr/bin/env python3

import sys
from hex_to_base64 import (
    base64_to_byteslike,
    base64_to_hex,
    base64_to_unicode,
)
from aes_encryption import cbc_decrypt
from utils import get_groups


def main():
    if len(sys.argv) != 2:
        print("""Usage:
              program filename

              filename - file whose contents will be transformed.
              """)
        sys.exit(84)
    try:
        with open(sys.argv[1]) as f:
            key = f.readline()
            if key == '':
                sys.exit(84)
            key = key.strip()
            IV = f.readline()
            if IV == '':
                sys.exit(84)
            IV = IV.strip()
            ciphertext = f.readline()
            if ciphertext == '':
                sys.exit(84)
            ciphertext = ciphertext.strip()
    except:
        sys.exit(84)

    # need = 'SW4gU2VwdGVtYmVyIDE5ODQsIEkgc3RhcnRlZCB3cml0aW5nIEdOVSBFbWFjcywgd2hpY2ggd2FzIG15IHNlY29uZAppbXBsZW1lbnRhdGlvbiBvZiBFbWFjcywgYW5kIGJ5IGVhcmx5IDE5ODUsIGl0IHdhcyB3b3JraW5nLiBJIGNvdWxkCnVzZSBpdCBmb3IgYWxsIG15IGVkaXRpbmcsIHdoaWNoIHdhcyBhIGJpZyByZWxpZWYsIGJlY2F1c2UgSSBoYWQgbm8KaW50ZW50aW9uIG9mIGxlYXJuaW5nIHRvIHVzZSBWSSwgdGhlIFVOSVggZWRpdG9yLiBbTGF1Z2h0ZXJdIFNvLCB1bnRpbAp0aGF0IHRpbWUsIEkgZGlkIG15IGVkaXRpbmcgb24gc29tZSBvdGhlciBtYWNoaW5lLCBhbmQgc2F2ZWQgdGhlCmZpbGVzIHRocm91Z2ggdGhlIG5ldHdvcmssIHNvIHRoYXQgSSBjb3VsZCB0ZXN0IHRoZW0uIEJ1dCB3aGVuIEdOVQpFbWFjcyB3YXMgcnVubmluZyB3ZWxsIGVub3VnaCBmb3IgbWUgdG8gdXNlIGl0LCBpdCB3YXMgYWxzbyAtLSBvdGhlcgpwZW9wbGUgd2FudGVkIHRvIHVzZSBpdCB0b28uCgpTbyBJIGhhZCB0byB3b3JrIG91dCB0aGUgZGV0YWlscyBvZiBkaXN0cmlidXRpb24uIE9mIGNvdXJzZSwgSSBwdXQgYSBjb3B5CmluIHRoZSBhbm9ueW1vdXMgRlRQIGRpcmVjdG9yeSwgYW5kIHRoYXQgd2FzIGZpbmUgZm9yIHBlb3BsZSB3aG8gd2VyZSBvbgp0aGUgbmV0LiBUaGV5IGNvdWxkIHRoZW4ganVzdCBwdWxsIG92ZXIgYSB0YXIgZmlsZSwgYnV0IGEgbG90IG9mCnByb2dyYW1tZXJzIHRoZW4gZXZlbiB3ZXJlIG5vdCBvbiB0aGUgbmV0IGluIDE5ODUu'
    # print(base64_to_unicode(need))
    plaintext = cbc_decrypt(ciphertext, key, IV)
    print(plaintext)


if __name__ == '__main__':
    try:
        main()
    except:
        sys.exit(84)