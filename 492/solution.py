from typing import List

class Solution:
    def _max_leq(self, low: int, high: int, target: int) -> int:
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
            if area % width != 0:
                continue

            length = area // width
            candidate = self._max_leq(width, area, length)

            if candidate < width:
                continue
            if candidate == length:
                dimensions = [length, width]

        return dimensions
