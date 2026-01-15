class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = sum(1 for num in nums if num < 0)
        pos = sum(1 for num in nums if num > 0)
        return max(neg, pos)
