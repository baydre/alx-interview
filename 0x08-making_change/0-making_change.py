#!/usr/bin/python3
"""
alx-interview:
    Task.0: Change comes from within
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize a list to store the fewest number of coins needed for each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Iterate through each coin value
    for coin in coins:
        # Update dp[j] if using this coin would reduce the number of coins needed to make amount j
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)
    
    # If dp[total] is still float('inf'), it means total cannot be met by any number of coins
    if dp[total] == float('inf'):
        return -1
    
    return dp[total]
