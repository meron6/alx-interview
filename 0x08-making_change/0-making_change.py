#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """
    Return the minimum number of coins needed to meet a given total.
    
    Args:
        coins (list of ints): a list of coins of different values.
        total (int): total value to be met.
        
    Return:
        int: fewest number of coins needed to make the total.
             Return -1 if the total cannot be met by any number of coins.
    """
    if total <= 0:
        return 0

    # Initialize a list for storing the fewest number of coins for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make the total 0

    # Loop over each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be made with the given coins
    return dp[total] if dp[total] != float('inf') else -1
