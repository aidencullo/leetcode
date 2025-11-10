class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        n = len(position)
        evens = sum(1 if x % 2 == 0 else 0 for x in position)
        odds = sum(1 if x % 2 == 1 else 0 for x in position)
        return min(evens, odds)
