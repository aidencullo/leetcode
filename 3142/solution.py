class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        return all(
            (i == rows - 1 or grid[i][j] == grid[i + 1][j]) and
            (j == cols - 1 or grid[i][j] != grid[i][j + 1])
            for i in range(rows) for j in range(cols)
        )
