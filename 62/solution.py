class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for i in range(m)]
        grid[0][0] = 1

        def get(r, c):
            if not (0 <= r < m and 0 <= c < n):
                return 0
            return grid[r][c]

        for row in range(m):
            for col in range(n):
                grid[row][col] += get(row, col - 1)
                grid[row][col] += get(row - 1, col)

        return grid[m - 1][n - 1]
