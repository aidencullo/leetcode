# 189. Rotate Array
from typing import List

class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        if len(nums) % 2 == 0:
            self.rotateEven(nums, k)
        else:
            self.rotateOdd(nums, k)


    def rotateOdd(self, nums: List[int], k: int) -> None:
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

    def rotateEven(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        cycles = k
        cycle_len = n // k
        for start in range(k):
            pos = start
            el = nums[start]
            for _ in range(cycle_len):
                next_index = (pos + k) % n
                next_el = nums[next_index]
                nums[next_index] = el
                el = next_el
                pos = next_index
            
            
            
