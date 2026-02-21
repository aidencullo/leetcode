class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if len(set(tuple(point) for point in points)) < len(points):
            return False

        def calculate_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2

            return (y2 - y1) / (x2 - x1)

        from itertools import pairwise

        p1, p2 = points[0], points[1]
        slope = calculate_slope(p1, p2)

        for a, b in pairwise(points):
            if slope != calculate_slope(a, b):
                return False

        return True
        

        
