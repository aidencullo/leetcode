class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        diff = max(nums) - min(nums)
        if diff > 2 * k:
            return diff - 2 * k
        return 0
