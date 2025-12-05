class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        m = len(piles)
        n = m // 3
        i = m - 2
        coins = 0
        for _ in range(n):
            coins += piles[i]
            i -= 2
        return coins
