class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:

        z_area = sum(1 if item else 0 for row in grid for item in row)
        x_area = sum(max(row) for row in grid)
        y_area = sum(max(col) for col in zip(*grid))

        return z_area + y_area + x_area
