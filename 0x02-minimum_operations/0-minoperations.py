#!/usr/bin/python3
"""
This method calculates the minimum number of operations required
to achieve exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates and returns the minimum number of operations required
    to achieve exactly n H characters in the file.
    """
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
