#!/usr/bin/python3

def validUTF8(data):
    """Determines if the given list of integers represents valid UTF-8 encoding.

    Args:
        data (list of int): List of integers representing bytes.

    Returns:
        bool: True if data represents valid UTF-8 encoding, otherwise False.
    """
    bit_count = 0
    
    for byte in data:
        if bit_count == 0:
            # Determine how many leading 1 bits are in the current byte
            if (byte >> 7) == 0b0:
                # 1-byte character
                bit_count = 0
            elif (byte >> 5) == 0b110:
                # 2-byte character
                bit_count = 1
            elif (byte >> 4) == 0b1110:
                # 3-byte character
                bit_count = 2
            elif (byte >> 3) == 0b11110:
                # 4-byte character
                bit_count = 3
            else:
                # Invalid start byte
                return False
        else:
            # Check if the byte is a valid continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            bit_count -= 1

    # Ensure there are no pending bytes that are not properly closed
    return bit_count == 0
