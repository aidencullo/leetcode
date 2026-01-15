class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = [x for x in nums if x < 0]
        pos = [x for x in nums if x > 0]
        return max(len(neg), len(pos))
