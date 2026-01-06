class Solution:
    def mySqrt(self, x: int) -> int:
        i = bisect.bisect_left(range(x + 1), x, key=lambda y: y ** 2)
        if i ** 2 != x:
            return i - 1
        return i
