#!/usr/bin/python3
"""Prime Game"""


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    """Generate a list of prime numbers up to n"""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    cumulative_primes = [0] * (max_num + 1)

    for i in range(1, max_num + 1):
        cumulative_primes[i] = cumulative_primes[i - 1] + \
            (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if cumulative_primes[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
