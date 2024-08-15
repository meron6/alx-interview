#!/usr/bin/python3
"""Reads from standard input and computes metrics.

This script prints the following statistics after every ten lines or upon a keyboard interruption (CTRL + C):
    - The total file size read up to that point.
    - The count of each read status code up to that point.
"""

def print_stats(size, status_codes):
    """Prints the accumulated metrics.

    Args:
        size (int): The total read file size.
        status_codes (dict): The count of status codes.
    """
    print(f"File size: {size}")
    for key in sorted(status_codes.keys()):
        print(f"{key}: {status_codes[key]}")

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 0
            count += 1

            parts = line.split()

            try:
                size += int(parts[-1])
            except (IndexError, ValueError):
                continue

            try:
                if parts[-2] in valid_codes:
                    status_codes[parts[-2]] = status_codes.get(parts[-2], 0) + 1
            except IndexError:
                continue

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
