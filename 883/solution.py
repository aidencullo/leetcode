class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        x = [0] * 50
        y = [0] * 50
        z_area = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                y[j] = max(y[j], grid[i][j])
                z_area += 1 if grid[i][j] else 0


        x_area = sum(max(row) for row in grid)
        y_area = sum(y)

        return z_area + y_area + x_area
