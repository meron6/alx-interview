def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.
    :param n: Number of rows in Pascal's Triangle.
    :return: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        # Calculate the intermediate values
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle


def print_left(triangle):
    """
    Prints the triangle in a left-aligned format to demonstrate data structure
    """
    for row in triangle:
        print(" ".join(map(str, row)))


def print_centre(triangle):
    """
    Prints the triangle in a conventional centred format
    """
    max_width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))


def main():
    """
    Create and populate Pascal's Triangle
    and then print it in two formats
    """
    print("---------------------")
    print("| Pascal's Triangle |")
    print("---------------------\n")

    n = 8  # Number of rows
    triangle = pascal_triangle(n)

    print("Left-aligned Pascal's Triangle:")
    print_left(triangle)

    print("\nCentred Pascal's Triangle:")
    print_centre(triangle)


if __name__ == "__main__":
    main()

