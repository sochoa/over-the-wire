#!/usr/bin/env python3
"""
This code really doesn't work.  I didn't want to just 
throw it away, so keep it here in case I want to hack 
on it later.
"""
import sys 
import json
import base64
from urllib.parse import unquote, urlencode

def xor_strings(s, t) -> bytes:
    """xor two strings together."""
    if isinstance(s, str):
        # Text strings contain single characters
        return b"".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        # Python 3 bytes objects contain integer values in the range 0-255
        return bytes([a ^ b for a, b in zip(s, t)])

ciphertext = base64.b64decode(unquote("ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D").encode('utf8'))
actual = {
    "showpassword":"no", 
    "bgcolor":"#ffffff"
}
actual = json.dumps(actual)
actual = base64.b64encode(actual.encode('utf8'))
key = xor_strings(actual,ciphertext)
key = base64.b64encode(key)
print(key)
key = urlencode(key.decode('ascii'))
