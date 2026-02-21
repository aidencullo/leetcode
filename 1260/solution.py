from typing import List

def make_double_list(rows, cols):
    return [[None for _ in range(cols)] for _ in range(rows)]

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        def shift_first_row(old):
            import copy
            new = copy.deepcopy(old)
            from itertools import product

            rows = len(new)
            cols = len(new[0])
            for row in range(rows):
                old_row = (row - 1) % rows
                old_col = 0
                col = 0
                new[row][col] = old[old_row][old_col]

            return new


        def shift(old):
            return [row[-1:] + row[:-1] for row in old]

        for i in range(k):
            grid = shift(grid)
            grid = shift_first_row(grid)

        return grid
