from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def swap(grid, p1, p2):
            xs, ys = p1
            xe, ye = p2
            grid[xs][ys], grid[xe][ye] = grid[xe][ye], grid[xs][ys]
        
        def shift(grid):
            cols = list(zip(*matrix))
            new_cols = cols[-1] + cols[1:]
            new = [list(r) for r in zip(*cols)]
            swap(new, (0, 0), (0, len(grid) - 1))
            return new
        
        for i in range(k):
            grid = shift(grid)

        return grid
