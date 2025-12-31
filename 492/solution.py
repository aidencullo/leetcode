class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for width in range(math.isqrt(area), 0, -1):
            if area % width == 0:
                return [area // width, width]
