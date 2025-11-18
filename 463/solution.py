class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def in_grid(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        def is_water(r, c):
            return not in_grid(r, c) or not grid[r][c]

        def is_land(r, c):
            return not is_water(r, c)
        
        def dfs(r, c):
            if is_water(r, c):
                return False

            if (r, c) in seen:
                return

            seen.add((r, c))

            nonlocal perimeter

            perimeter += is_water(r + 1, c) + is_water(r - 1, c) + is_water(r, c + 1) + is_water(r, c - 1)

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            

        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        seen = set()
        for i, j in product(range(rows), range(cols)):
            if is_land(i, j):
                dfs(i, j)
                break
        return perimeter
