#!/usr/bin/python3
"""Task 0 solution"""


def makeChange(coins, total):
    """Finds smallest number of coins to make change"""

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    total_coins = 0

    for coin in coins:
        num_coins = 0
        if total >= coin:
            num_coins = total // coin
            total_coins += num_coins
            total -= coin * num_coins

    if total == 0:
        return total_coins
    return -1
