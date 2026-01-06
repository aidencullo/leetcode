class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            k = (l + r) // 2
            y = k ** 2

            if x >= y:
                l = k + 1
            else:
                r = k - 1
        return r
