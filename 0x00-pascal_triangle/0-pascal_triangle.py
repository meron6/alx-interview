def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    Returns a list of lists of integers.
    """
    if n <= 0:
        return []  # Return an empty list for non-positive n

    triangle = [[1]]  # Initialize the first row with [1]

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # Start the new row with 1

        # Calculate the middle elements of the row
        for j in range(1, i):
            new_elem = prev_row[j - 1] + prev_row[j]
            new_row.append(new_elem)

        new_row.append(1)  # End the row with 1
        triangle.append(new_row)  # Add the new row to the triangle

    return triangle

# Example usage:
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)
