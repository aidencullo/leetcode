class Solution:
    def mySqrt(self, x: int) -> int:
        i = bisect.bisect_left(range(x + 1), x + 1, key=lambda y: y ** 2)
        return i - 1
