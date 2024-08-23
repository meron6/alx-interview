#!/usr/bin/python3


def validUTF8(data):
    """Determines if given data represents valid UTF-8 encoding

    Args:
        data: list of integers

    Returns:
        True if valid UTF-8 encoding, otherwise False
    """
    bit_count = 0
    for n in data:
        mask = 1 << 7
        if not bit_count:
            while n & mask:
                bit_count += 1
                mask >>= 1
            if bit_count > 4:
                return False
        elif n >> 6 != 2:
            return False
        if bit_count:
            bit_count -= 1
    return bit_count == 0
