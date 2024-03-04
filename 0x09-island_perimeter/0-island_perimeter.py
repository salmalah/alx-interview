#!/usr/bin/python3
"""
This module is to define contains a function to
calculate the perimeter of an island
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid
    Returns: the perimeter of the island.
    """
    perimet = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for o, row in enumerate(grid):
        m = len(row)
        for l, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                o == 0 or (len(grid[o - 1]) > l and grid[o - 1][l] == 0),
                l == m - 1 or (m > l + 1 and row[l + 1] == 0),
                i == n - 1 or (len(grid[o + 1]) > j and grid[o + 1][l] == 0),
                l == 0 or row[l - 1] == 0,
            )
            perimet += sum(edges)
    return perimet
