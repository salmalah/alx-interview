#!/usr/bin/python3
"""Prime game module"""

def if_Prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_Prime_count(num):
    """Counts the prime numbers up to a given number."""
    count = 0
    for n in range(1, num + 1):
        if if_Prime(n):
            count += 1
    return count

def isWinner(x, nums):
    """Determines who the winner of the game is."""
    ben = 0
    maria = 0
    if x <= 0 or not nums:
        return None
    for num in nums:
        prime_count = get_Prime_count(num)
        if prime_count % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None
