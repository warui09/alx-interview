#!/usr/bin/python3
"""
Returns a list of lists of integers representing the Pascal’s
triangle of n
    - Returns an empty list if n <= 0
    - n is assumed to always be an integer
"""

def pascal_triangle(n):
    """ Return a list of integers representing Pascal's triangle"""

    triangle = []

    if n <= 0:
        return triangle

    # outer loop to keep track of rows
    for i in range(1, n + 1):
        # create row
        row = []

        # inner loop for keeping track of elements in a row
        for j in range(i):
            # calculate element
            if j == 0 or j == i - 1 or i == 1:
                element = 1
            else:
                element = triangle[i - 2][j - 1] + triangle[i - 2][j]

            # append element to row
            row.append(element)


        # append row to triangle
        triangle.append(row)

    # return triangle
    return triangle
