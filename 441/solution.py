class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            k = (r + l) // 2
            steps = k * (k + 1) / 2

            if n >= steps:
                l = k + 1
            else:
                r = k - 1

        return r
                
