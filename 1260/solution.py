class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        def flatten(grid):
            return [grid[r][c] for r in range(len(grid)) for c in range(len(grid[0]))]

        def shift(lst, k):
            return lst[-k:] + lst[:-k]

        def unflatten(lst):
            cols = len(grid[0])
            return [[lst[r * cols + c] for c in range(cols)] for r in range(len(grid))]

        k %= len(grid) * len(grid[0])
        flattened = flatten(grid)
        shifted = shift(flattened, k)
        unflattened = unflatten(shifted)
        return unflattened
        
