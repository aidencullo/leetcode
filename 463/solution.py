class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def is_water(r, c):
            if not 0 <= r < len(grid):
                return True
            if not 0 <= c < len(grid[0]):
                return True

            return not grid[r][c]
        
        def dfs(r, c):
            if not 0 <= r < len(grid):
                return
            if not 0 <= c < len(grid[0]):
                return

            if not grid[r][c]:
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
        # from collections import product
        # pairs = product(range(rows), range(cols))
        # for i, j in pairs:
        #         dfs(i, j)
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                dfs(i, j)
        return perimeter
