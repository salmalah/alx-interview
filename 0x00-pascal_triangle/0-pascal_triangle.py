#!/usr/bin/python3
"""
Pascal's Triangle of n
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        r = [1]
        for j in range(1, i):
            r.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        r.append(1)
        triangle.append(r)

    return triangle
