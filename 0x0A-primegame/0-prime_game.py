#!/usr/bin/python3
"""Task 0"""


def SieveOfEratosthenes(n):
    """Returns all prime numbers from 1 through n"""

    nums = [True for i in range(n + 1)]
    primes = []
    p = 2
    while p * p <= n:
        if nums[p] == True:
            for i in range(p * p, n + 1, p):
                nums[i] = False
        p += 1

    for p in range(2, n + 1):
        if nums[p]:
            primes.append(p)

    return primes


def isWinner(x, nums):
    """Determines the winner of each round of a game of
    eliminating primes and their multiples"""

    ben_wins = 0
    maria_wins = 0

    for num in nums:
        primes = SieveOfEratosthenes(num)
        len_primes = len(primes)
        integers = list(range(1, num + 1))
        counter = 0

        if len_primes == 0:
            ben_wins += 1
            continue

        # Maria's strategy: always choose the largest prime available
        while counter < len(primes):
            max_prime = primes[-1]
            integers = list(filter(lambda x: x % max_prime != 0, integers))
            largest_int = max(integers)
            if len(integers) == 0:
                maria_wins += 1
                break
            counter += 1

        if len(integers) == 0:
            continue

        # Ben's strategy: always choose the smallest prime available
        while counter < len(primes):
            min_prime = primes[0]
            integers = list(filter(lambda x: x % min_prime != 0, integers))
            if len(integers) == 0:
                ben_wins += 1
                break
            counter += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
