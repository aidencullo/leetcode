from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def backtrack(i, last, count):
            nonlocal lis
            
            if i == len(nums):
                lis = max(lis, count)
                return

            backtrack(i + 1, last, count)
            if last < nums[i]:
                backtrack(i + 1, nums[i], count + 1)
            

        lis = 0
        backtrack(0, -math.inf, 0)
        return lis
