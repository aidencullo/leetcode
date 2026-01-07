from typing import List
import math
from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def backtrack(i, last):
            if i == len(nums):
                return 0
            # skip current
            lis = backtrack(i + 1, last)
            # take current if increasing
            if last < nums[i]:
                lis = max(lis, backtrack(i + 1, nums[i]) + 1)
            return lis

        return backtrack(0, -math.inf)
