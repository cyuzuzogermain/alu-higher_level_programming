#!/usr/bin/python3
"""
Function that returns a list of lists
representing Pascal's Triangle of n.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        List of lists of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        # Start each row with 1
        row = [1]
        # Compute the values in between
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        # End each row with 1
        row.append(1)
        triangle.append(row)

    return triangle
