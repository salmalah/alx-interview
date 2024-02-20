#!/usr/bin/python3
"""
This module is to define rotates a 2D matrix 90 degrees clockwise.
"""


def transpose(matrix):
    """ transport matrix
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_rows(matrix):
    """
    reverse rows
    return revers"""
    n = len(matrix)
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    """
    transpose(matrix)
    reverse_rows(matrix)
