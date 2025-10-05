class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols - 1):
                if grid[i][j] == grid[i][j + 1]:
                    return False
        # grid_transpose = [[grid[col][row] for col in range(n)] for row in range(n)]
        list_of_tuples = list(map(tuple, grid))
        print(list_of_tuples)
        if len(set(list_of_tuples)) != 1:
            return False
        return True
