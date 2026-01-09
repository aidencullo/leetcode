class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0

        for r in range(rows):
            for c in range(cols):
                h = grid[r][c]
                if h == 0:
                    continue

                area += 2

                area += max(h - (grid[r-1][c] if r > 0 else 0), 0)
                area += max(h - (grid[r+1][c] if r < rows-1 else 0), 0)
                area += max(h - (grid[r][c-1] if c > 0 else 0), 0)
                area += max(h - (grid[r][c+1] if c < cols-1 else 0), 0)

        return area
