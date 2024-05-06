#!/usr/bin/python3
"""0. Island Perimeter"""


def island_perimeter(grid):
    """Return perimeter of an island"""

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbors = 0
            if grid[i][j] == 1:
                # get neighbors
                if j > 0 and grid[i][j - 1] == 1:
                    neighbors += 1
                if i > 0 and grid[i - 1][j] == 1:
                    neighbors += 1
                if j < len(grid[i]) - 2 and grid[i][j + 1] == 1:
                    neighbors += 1
                if i < len(grid) - 2 and grid[i + 1][j] == 1:
                    neighbors += 1

                if neighbors == 0:
                    perimeter += 4
                elif neighbors == 1:
                    perimeter += 3
                elif neighbors == 2:
                    perimeter += 2
                elif neighbors == 3:
                    perimeter += 1

    return perimeter
