from typing import List

def make_double_list(rows, cols):
    return [[None for _ in range(cols)] for _ in range(rows)]

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        def shift_first_row(old):
            import copy
            new = copy.deepcopy(old)

            rows = len(new)
            for row in range(rows):
                new[row][0] = old[row - 1][0]

            return new


        def shift(old):
            return [row[-1:] + row[:-1] for row in old]

        for i in range(k):
            grid = shift(grid)
            grid = shift_first_row(grid)

        return grid
