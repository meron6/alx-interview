#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1

            if count % 10 == 0:
                print_stats(size, status_codes)

            parts = line.split()

            if len(parts) < 7:
                continue  # Skip lines that don't have the expected number of parts

            try:
                size += int(parts[-1])
            except ValueError:
                pass  # Ignore lines with invalid file size

            try:
                status_code = int(parts[-2])
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except ValueError:
                pass  # Ignore lines with invalid status code

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
