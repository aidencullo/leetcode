class Solution:
    def __init__(self):
        self.memo = {}
        self.memo[0] = 1
        self.memo[1] = 1

    def numTrees(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        total = 0
        for i in range(1, n + 1):
            total += self.numTrees(i - 1) * self.numTrees(n - i)
        self.memo[n] = total
        return self.memo[n]
