#!/usr/bin/python3

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of coin denominations.
        total (int): The target amount to be achieved.

    Returns:
        int: The fewest number of coins needed to meet the total, or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    # Initialize dp array with infinity for all values except 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins to make the amount 0

    # Loop through each coin and build up the dp table
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be made with the given coins
    return dp[total] if dp[total] != float('inf') else -1
