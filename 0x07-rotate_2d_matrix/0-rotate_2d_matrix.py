#!/usr/bin/python3
"""
def rotate_2d_matrix(matrix):
    """
    Rotate a 2D square matrix 90 degrees clockwise in-place.
    
    Args:
        matrix (list of list of int): 2D square matrix.
        
    Returns:
        None
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
