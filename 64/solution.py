import functools
import math

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        from copy import deepcopy
        min_path_grid = deepcopy(grid)
        rows = len(grid)
        cols = len(grid[0])

        def get(r, c):
            if 0 <= r < rows and 0 <= c < cols:
                return grid[r][c]
            return math.inf
            
        
        for r in range(rows):
            for c in range(cols):
                min_path_grid[r][c] += min(get(r - 1, c), get(r, c - 1))
        return min_path_grid[-1][-1]
        
