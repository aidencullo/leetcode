class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def calculate_area(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3

            return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
        
        max_area = 0
        for p1 in points:
            for p2 in points:
                for p3 in points:
                    max_area = max(max_area, calculate_area(p1, p2, p3))
        return max_area
