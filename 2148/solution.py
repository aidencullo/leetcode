from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        low = min(nums)
        high = max(nums)
        return len(nums) - nums.count(low) - nums.count(high)
