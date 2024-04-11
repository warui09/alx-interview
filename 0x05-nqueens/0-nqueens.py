#!/usr/bin/python3
"""solves nqueens challenge"""

import sys


def nqueens(q, size):
    """get the square to place a queen on row"""

    solutions = []
    if len(q) == size:
        return [q]
    for i in range(size):
        valid = True
        for j in range(len(q)):
            if q[j] == i or q[j] == i + len(q) - j or q[j] == i - len(q) + j:
                valid = False
                break
        if valid:
            solutions.extend(nqueens(q + [i], size))
    return solutions


def main():
    """Run the code"""

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if size < 4:
        print("N must be at least 4")
        exit(1)

    solutions = nqueens([], size)
    for solution in solutions:
        points = []
        for index, num in enumerate(solution):
            points.append([index, num])
        print(points)


if __name__ == "__main__":
    main()
