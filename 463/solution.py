class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def in_grid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        def is_water(r, c):
            return not in_grid(r, c) or not grid[r][c]
        
        def dfs(r, c):
            if is_water(r, c):
                return False
            
            return is_water(r + 1, c) + is_water(r - 1, c) + is_water(r, c + 1) + is_water(r, c - 1)

        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        for i, j in product(range(rows), range(cols)):
                perimeter += dfs(i, j)
        return perimeter
