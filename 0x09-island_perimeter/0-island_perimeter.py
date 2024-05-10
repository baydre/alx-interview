#!/usr/bin/python3
"""
alx-interview:
    island_Perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of
    island described.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:  # Check top
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check left
                    perimeter -= 2
    return perimeter
