from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        low = nums[0] * nums[1] * nums[-1]
        high = nums[-3] * nums[-2] * nums[-1]
        return max(low, high)
