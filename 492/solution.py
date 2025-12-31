from typing import List

class Solution:
    def _max_leq(self, low: int, high: int, target: int) -> int:
        return low + bisect.bisect_left(range(low, high + 1), target)
        left, right = low, high
        while left <= right:
            mid = (left + right) // 2
            if mid <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    def constructRectangle(self, area: int) -> List[int]:
        dimensions = None
        for width in range(1, area + 1):
            length = area // width
            
            if area % width != 0:
                continue
            if length < width:
                continue

            dimensions = [length, width]

        return dimensions
