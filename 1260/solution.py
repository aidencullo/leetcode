from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        def shift(grid):
            cols = list(zip(*matrix))
            last_col = cols[-1]
            new_first_col = last_col[-1] + last_col[1:]
            new_remaining_cols = cols[1:]
            new_cols = new_first_col + new_remaining_cols
            new = [list(r) for r in zip(*cols)]
            return new
        
        for i in range(k):
            grid = shift(grid)

        return grid
