#!/usr/bin/env python3
import sys

def print_stats(file_size, status_codes):
    print(f"File size: {file_size}")
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")

if __name__ == "__main__":
    file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) != 7:
                continue  # Skip lines that don't match the expected format
            
            try:
                status_code = int(parts[6])
                if status_code in status_codes:
                    status_codes[status_code] += 1
                file_size += int(parts[5])
            except ValueError:
                continue  # Skip lines with invalid status codes or file sizes

            if line_count % 10 == 0:
                print_stats(file_size, status_codes)
                file_size = 0
                status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    except KeyboardInterrupt:
        print_stats(file_size, status_codes)
