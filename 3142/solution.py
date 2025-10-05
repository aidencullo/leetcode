class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        def is_equal_below(i, j):
            if i == rows - 1:
                return True
            return grid[i][j] == grid[i + 1][j]

        def is_different_right(i, j):
            if j == cols - 1:
                return True
            return grid[i][j] != grid[i][j + 1]

        rows = len(grid)
        cols = len(grid[0])
        return all(
            is_equal_below(i, j) and is_different_right(i, j)
            for i in range(rows)
            for j in range(cols)
        )
