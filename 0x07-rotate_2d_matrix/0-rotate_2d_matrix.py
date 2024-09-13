#!/usr/bin/python3
"""
A function to rotate an nxn 2D matrix 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D square matrix 90 degrees clockwise in-place.
    Args:
        matrix (list): 2D square matrix.
    Returns:
        None.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
