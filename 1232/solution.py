from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def calc_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2

            if x1 == x2:
                return math.inf

            return (y2 - y1) / (x2 - x1)


        slope = calc_slope(coordinates[0], coordinates[1])

        for a, b in pairwise(coordinates):
            if slope != calc_slope(a, b):
                return False

        return True
        
