class Solution:
    # Time: O(n²) | Space: O(1)
    def surfaceArea(self, grid: List[List[int]]) -> int:
        def inside_grid(pair):
            return (0 <= pair[0] < len(grid)
                    and 0 <= pair[1] < len(grid[0]))

        def outside_grid(pair):
            return not inside_grid(pair)

        def get_pair(p):
            r, c = p
            return grid[r][c]
        
        def surface_between(p1, p2):
            if outside_grid(p2):
                return get_pair(p1)
            return 0 if get_pair(p1) < get_pair(p2) else get_pair(p1) - get_pair(p2)
        
        def calculate(r, c):
            surface_area = 0
            surface_area += surface_between((r, c), (r + 1, c))
            surface_area += surface_between((r, c), (r - 1, c))
            surface_area += surface_between((r, c), (r, c + 1))
            surface_area += surface_between((r, c), (r, c - 1))
            surface_area += 2 if grid[r][c] else 0
            return surface_area
        
        return sum(calculate(r, c) for r, c in product(range(len(grid)), range(len(grid[0]))))
            
