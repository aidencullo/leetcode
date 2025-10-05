class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols - 1):
                if grid[i][j] == grid[i][j + 1]:
                    return False

        transpose = [list(row) for row in zip(*grid)]
        rows, cols = cols, rows

        for i in range(rows):
            for j in range(cols - 1):
                if transpose[i][j] != transpose[i][j + 1]:
                    return False

        return True
