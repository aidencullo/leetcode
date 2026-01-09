class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        def inside_grid(pair):
            return (0 <= pair[0] < len(grid)
                    and 0 <= pair[1] < len(grid[0]))

        def outside_grid(pair):
            return not inside_grid(pair)
        
        def surface_between(p1, p2):
            if outside_grid(p2):
                return grid[p1[0], p1[1]]
            return 0 if grid[p1[0], p1[1]] < grid[p2[0], p2[1]] else grid[p2[0], p2[1]]
        
        def calculate(r, c):
            surface_area = 0
            surface_area += surface_between((r, c), (r + 1, c))
            surface_area += surface_between((r, c), (r - 1, c))
            surface_area += surface_between((r, c), (r, c + 1))
            surface_area += surface_between((r, c), (r, c - 1))
            return surface_area
        
        return sum(print(r) for r, c in product(range(len(grid)), range(len(grid[0]))))
            
