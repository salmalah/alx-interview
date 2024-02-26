#!/usr/bin/python3
"""
This Moduleis to define 
change with the fewest number of coins
"""

def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total
    Returns: Fewest number of coins needed to meet total
    or -1 if not possible
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
