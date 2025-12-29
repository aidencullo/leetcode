class Solution:
    def arrangeCoins(self, n: int) -> int:
        levels = 0
        while n > 0:
            levels += 1
            n -= levels

        if n < 0:
            levels -= 1

        return levels
