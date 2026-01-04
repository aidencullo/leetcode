class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = 0
        
        for row in grid:
            negative_i = bisect.bisect_right(list(reversed(row)), -1)
            negatives += negative_i

        return negatives
