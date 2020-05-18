#!/usr/bin/env python3

import argparse
import base64


def decode_base64(some_bytes):
    return base64.b64decode(some_bytes)

def reverse_string(s):
    return s[::-1]

def hex_to_binary(s):
    scale = 16
    num_bits = 8
    return bin(int(s, scale)).zfill(num_bits)

parser = argparse.ArgumentParser()
parser.add_argument("secret", type=str)
args = parser.parse_args()
secret = args.secret
before, secret = secret, hex_to_binary(secret) # reverse of bin2hex
print(before, secret)
before, secret = secret, reverse_string(secret) # reverse of strrev
print(before, secret)
before, secret = secret, decode_base64(secret)
print(before, secret)
