class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        mem = {}

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return math.inf

            val = grid[r][c]

            if r == rows - 1 and c == cols - 1:
                return val

            

            if (r, c) not in mem:
                mem[(r, c)] = val + min(dfs(r, c + 1), dfs(r + 1, c))

            return mem[(r, c)]

        return dfs(0, 0)
