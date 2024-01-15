#!/usr/bin/python3
"""
This module is the calculates the fewest number of operations needed
to result in exactly n H characters
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters
    Returns: The minimum number of operations needed.
    """
    if n <= 1:
        return 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n
