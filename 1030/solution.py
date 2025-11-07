class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        grid  = [[0] * cols for i in range(rows)]
        for row in range(rows):
            for col in range(cols):
                grid[row][col] = abs(row - rCenter) + abs(col - cCenter)
        distances  = [(grid[row][col], [row, col]) for row in range(rows) for col in range(cols)]
        distances.sort()
        return [pair for distance, pair in distances]
