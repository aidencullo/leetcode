class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def in_grid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        def is_water(r, c):
            return not in_grid(r, c) or not grid[r][c]
        
        def dfs(r, c):
            if is_water(r, c):
                return
            
            if (r, c) in seen:
                return

            seen.add((r, c))
            
            nonlocal perimeter

            if is_water(r + 1, c):
                perimeter += 1
            if is_water(r - 1, c):
                perimeter += 1
            if is_water(r, c + 1):
                perimeter += 1
            if is_water(r, c - 1):
                perimeter += 1

            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)


        perimeter = 0
        seen = set()
        from itertools import product
        rows = len(grid)
        cols = len(grid[0])
        pairs = product(range(rows), range(cols))
        for i, j in pairs:
                dfs(i, j)
        return perimeter
