#!/usr/bin/python3
"""Module containing a function that checks if a list of ints is a valid
utf8 character"""

def validUTF8(data):
    """Checks if a list of integers represents a valid UTF-8 encoding.

    Args:
        data (list of int): List of integers representing bytes.

    Returns:
        bool: True if data represents valid UTF-8 encoding, otherwise False.
    """
    n_bytes = 0
    for byte in data:
        # Convert byte to binary string with leading zeroes
        bi_str = format(byte, '#010b')[-8:]
        
        if n_bytes == 0:
            # Count the number of leading 1 bits
            for bit in bi_str:
                if bit == '0':
                    break
                n_bytes += 1

            # If n_bytes is 1 or more than 4, it's not valid
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check if continuation byte (should start with '10')
            if not (bi_str.startswith('10')):
                return False
        n_bytes -= 1

    # Ensure there are no pending bytes that are not properly closed
    return n_bytes == 0

if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # True

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115,
            32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # False

    data = [235, 140]
    print(validUTF8(data))  # False
