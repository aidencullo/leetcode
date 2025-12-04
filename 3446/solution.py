from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        def sort_diagonal(indices, reverse=False):
            diag = [grid[i][j] for i, j in indices]
            diag_sorted = sorted(diag, reverse=reverse)
            for (i, j), val in zip(indices, diag_sorted):
                grid[i][j] = val

        # Bottom-left diagonals
        for start_row in range(n):
            indices = [(r, c) for r, c in zip(range(start_row, n), range(n))]
            sort_diagonal(indices, reverse=True)

        # Top-right diagonals
        for start_col in range(1, n):
            indices = [(r, c) for r, c in zip(range(n), range(start_col, n))]
            sort_diagonal(indices)

        return grid
