#!/usr/bin/python3
"""
Making Change
"""


def make_change(coins, total):
    """
    Calculate the minimum number of coins required to make a given total.
    Args:
        coins (list of ints): denominations of coins available
        total (int): the total amount to make change for
    Returns:
        int: minimum number of coins needed, or -1 if change cannot be made
    """
    if total <= 0:
        return 0
    if not coins:
        return -1
    if total in coins:
        return 1

    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            coin_count += 1
        if total == 0:
            return coin_count
    return -1
