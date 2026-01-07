import functools
import math

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        path = math.inf

        @functools.cache
        def dfs(r, c, last):
            nonlocal path
            if not (0 <= r < rows and 0 <= c < cols):
                return
            val = grid[r][c]
            current = last + val
            if r == rows - 1 and c == cols - 1:
                path = min(current, path)
            dfs(r, c + 1, current)
            dfs(r + 1, c, current)

        dfs(0, 0, 0)
        return path
