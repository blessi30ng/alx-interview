#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes"""
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for x, row in enumerate(grid):
        m = len(row)
        for i, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                x == 0 or (len(grid[x - 1]) > i and grid[x - 1][i] == 0),
                i == m - 1 or (m > i + 1 and row[i + 1] == 0),
                x == n - 1 or (len(grid[x + 1]) > i and grid[x + 1][i] == 0),
                i == 0 or row[i - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
