#!/usr/bin/python3
"""
This module is to dWrite a method that determines if a
given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args: data :List of integers representing 1 byte of data each
    Returns bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_b = 0
    for char_d in data:
        byte = char_d & 0xff
        if num_b:
            if (byte >> 6 == 1 or byte >> 6 == 3):
                return False
            num_b -= 1
            continue

        while 7 - num_b and byte & (1 << (7 - num_b)):
            num_b += 1
        if num_b == 1 or num_b > 4:
            return False
        num_b = max(num_b - 1, 0)

    if num_b:
        return False
    return True
