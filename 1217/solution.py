class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(sum(x % 2 == 0 for x in position), sum(x % 2 == 1 for x in position))
