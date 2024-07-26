def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    Returns a list of lists representing the triangle.
    """
    if n <= 0:
        return []  # Return an empty list for non-positive n
    
    triangle = []  # Initialize an empty list to store the rows
    
    for i in range(n):
        row = []  # Initialize an empty list for the current row
        for j in range(i + 1):
            # Calculate the value at position (i, j) using binomial coefficient formula
            value = 1 if j == 0 or j == i else triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)
        triangle.append(row)
    
    return triangle

# Example usage:
if __name__ == "__main__":
    triangle_5 = pascal_triangle(5)
    for row in triangle_5:
        print(row)
