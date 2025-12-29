class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = bisect.bisect_left(range(num), num, key=lambda x: x ** 2)
        return x ** 2 == num
