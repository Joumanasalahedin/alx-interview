#!/usr/bin/python3
"""
Module to determine the fewest number of coins needed to meet a given total.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Returns:
        int: The fewest number of coins needed, or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total <= 0:
            break
        count += total // coin
        total %= coin

    return count if total == 0 else -1
