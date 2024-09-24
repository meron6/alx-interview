# 0x09. Island Perimeter

## Project Overview

This project involves creating a Python function to calculate the perimeter of an island in a grid. The grid is represented as a 2D list of integers, where:
- `0` represents water
- `1` represents land

The goal is to calculate the perimeter of the landmass (island) by analyzing the grid and determining the edges that contribute to the total perimeter.

## Learning Objectives

By the end of this project, you should be able to:

- Access and iterate over elements in a 2D array.
- Navigate through adjacent cells (horizontally and vertically).
- Apply conditions to determine whether a cell contributes to the perimeter of the island.
- Develop a method to count the edges that contribute to the island’s perimeter.
- Use nested loops and conditional statements in Python.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the folder of the project is mandatory
- Your code should use the PEP 8 style (version 1.7)
- You are not allowed to import any module
- All modules and functions must be documented
- All your files must be executable

## Installation

1. Clone the repository:
    ```bash
    $ git clone https://github.com/yourusername/alx-backend.git
    $ cd alx-backend/0x09-island_perimeter
    ```

2. Ensure your Python environment is set up correctly.

## Usage

1. Create a Python file named `0-island_perimeter.py` with the following content:

    ```python
    #!/usr/bin/python3
    """
    Module to calculate the perimeter of an island in a grid.
    """

    def island_perimeter(grid):
        """
        Returns the perimeter of the island described in grid.
        """
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        return perimeter
    ```

2. Make the file executable:
    ```bash
    $ chmod +x 0-island_perimeter.py
    ```

3. Test the function with a sample grid:
    ```python
    if __name__ == "__main__":
        grid = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
        print(island_perimeter(grid))  # Output should be 8
    ```

## Example

Given the following grid:
```python
grid = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]
