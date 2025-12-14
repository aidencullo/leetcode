class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        return sum(cost[i] for i in range(len(cost) - 1, -1, -1) if (len(cost) - 1 - i) % 3 != 2)
