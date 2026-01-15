class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = list(filter(lambda x: x < 0, nums))
        pos = list(filter(lambda x: x > 0, nums))
        return max(len(neg), len(pos))
