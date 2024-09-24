#!/usr/bin/python3
"""Module for computing the perimeter of an island."""


def island_perimeter(grid):
    """Computes the perimeter of an island without lakes."""
    perimeter = 0
    if not isinstance(grid, list):
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (j < len(grid[i - 1]) and grid[i - 1][j] == 0),
                j == m - 1 or (j + 1 < m and row[j + 1] == 0),
                i == n - 1 or (j < len(grid[i + 1]) and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
