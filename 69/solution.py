class Solution:
    def mySqrt(self, x: int) -> int:
        return bisect.bisect_left(range(x + 1), x, key=lambda x: i ** 2)


         # 367/solution.py:        x = bisect.bisect_left(range(num), num, key=lambda x: x ** 2)
