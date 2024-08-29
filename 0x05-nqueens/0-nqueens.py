#!/usr/bin/python3
"""N-Queens Problem Solver"""


class NQueens:
    """Solve the N-Queens problem."""

    def __init__(self, n: int):
        self.n = n
        self.solutions = []
        self.tracker = [-1] * n

    def valid(self, col: int) -> bool:
        """Check if placing a queen in the column is valid."""
        for i in range(col):
            if abs(self.tracker[i] - self.tracker[col]) in {0, col - i}:
                return False
        return True

    def helper(self, index: int, cols):
        """Recursive helper function to solve the problem."""
        if index == self.n:
            self.solutions.append(cols)
            return
        for i in range(self.n):
            self.tracker[index] = i
            if self.valid(index):
                self.helper(index + 1, cols + [i])

    def solve(self):
        """Run the recursive solver and return all solutions."""
        self.helper(0, [])
        return [[(i, sol[i]) for i in range(self.n)] for sol in self.solutions]


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueens(n)
    solutions = solver.solve()
    for res in solutions:
        print(res)
