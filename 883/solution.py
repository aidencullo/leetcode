class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:

        z_area = 0
        n = len(grid)

        for i in range(n):
            for j in range(n):
                z_area += 1 if grid[i][j] else 0


        x_area = sum(max(row) for row in grid)
        y_area = sum(max(col) for col in zip(*grid))

        return z_area + y_area + x_area
