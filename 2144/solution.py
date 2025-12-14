class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True);
        return sum((sum(cost[i:i+2]) for i in range(0, len(cost), 3)), 0);
