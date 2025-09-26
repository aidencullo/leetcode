# 189. Rotate Array
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        n = len(nums)
        k %= n
        if k == 0:
            return
        
        l, r = 0, k
        for i in range(n - 1):
            swap(l, r)
            l += 1
            r += 1
            l %= k
            r %= n
