from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        dimensions = None
        for width in range(1, math.isqrt(area) + 1):
            length = area // width
            
            if area % width != 0:
                continue
            if length < width:
                continue

            dimensions = [length, width]

        return dimensions
