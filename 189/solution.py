# 189. Rotate Array
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos = 0
        el = nums[pos]
        for _ in range(n):
            next_index = (pos + k) % n
            next_el = nums[next_index]
            nums[next_index] = el
            el = next_el
            pos = next_index
            
            
            
