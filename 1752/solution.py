from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        def is_sorted(arr: List[int]) -> bool:
            prev = float('-inf')
            for x in arr:
                if x < prev:
                    return False
                prev = x
            return True
        
        n = len(nums)
        for i in range(n):
            rotated = nums[i:] + nums[:i]
            if is_sorted(rotated):
                return True
        return False
