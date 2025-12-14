class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        i = 0
        total_cost = 0
        n = len(cost)
        while i < n:
            if (i + 1) % 3 == 0:
                i += 1
                continue
            total_cost += cost[i]
            i += 1
        return total_cost
