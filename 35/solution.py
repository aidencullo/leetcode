from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            k = (r + l) // 2
            el = nums[k]
            
            if target <= el:
                r = k - 1
            else:
                l = k + 1
            
        return l
