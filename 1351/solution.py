class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        import numpy as np

        np_grid = np.array(grid)

        rows, cols = np_grid.shape        
        min_axis = min(rows, cols)
        last_row = rows - 1
        last_col = cols - 1
