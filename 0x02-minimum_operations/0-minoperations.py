#!/usr/bin/python3
"""Module for minOperations function"""


def minOperations(n):
    """method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file"""
    if n <= 1:
        return 0

    operations = 0
    i = 2

    while n > 1:
        while n % i == 0:
            operations += i
            n //= i
        i += 1

    return operations
