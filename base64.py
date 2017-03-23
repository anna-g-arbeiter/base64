#!/usr/bin/env python3
import sys

class Base64Encoder:

    def encode(self, unicode_string=None):
        if(unicode_string is None):
            print("Provide a string to be encoded.")
            return
        get_bits = lambda c : bin(ord(c))[2:]
        # convert the passed string to its bit stream representation
        bit_stream = ""
        for char in unicode_string:
            bit_char = get_bits(char)
            if(bit_char.__len__() < 8):
                bit_char = (8 - bit_char.__len__())*'0' + bit_char
            bit_stream += bit_char

        # number of bytes must be divisible by 3
        # otherwise add zero bytes
        zero_bytes = (unicode_string.__len__() % 3)
        if(zero_bytes > 0):
            zero_bytes = 3 - zero_bytes
            bit_stream += zero_bytes * 8 * '0'

        # convert the bit stream to base64
        mapping = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        base64_stream = ""
        # a base64 encoded char has 6 bits
        # get the 6 bit decimal number at pos x of the bit stream:
        get_decimal = lambda x: int(bit_stream[x:x + 6], 2)
        # get the base64 encoded char from the mapping:
        get_base64_char = lambda x : mapping[x]

        index = 0
        while index < bit_stream.__len__():
            base64_decimal = get_decimal(index)
            base64_char = get_base64_char(base64_decimal)
            base64_stream += base64_char
            index += 6
        # The filling zero bytes are wrongly completely encoded with A.
        # For one earlier attached zero byte write instead one "=", and for two zero bytes two "="
        if(zero_bytes > 0):
            base64_stream = base64_stream[:base64_stream.__len__() - zero_bytes]
            base64_stream += zero_bytes * "="
        return base64_stream

def main():
    encoder = Base64Encoder()
    print(encoder.encode(sys.argv[1]))

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("One input string required.")
        sys.exit(-1)
    else:
        main()
