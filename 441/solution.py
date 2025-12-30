class Solution:
    def arrangeCoins(self, n: int) -> int:
        def arithmetic_series(x):
            return (x * (x + 1)) // 2

        x = bisect.bisect_left(range(n), n, key=arithmetic_series)
        if arithmetic_series(x) == n:
            return x
        else:
            return x - 1
