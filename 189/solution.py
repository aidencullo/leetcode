# 189. Rotate Array
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(left, right):
            nums[left], nums[right] = nums[right], nums[left]

        def shift_one():
            el = nums[-1]
            for i in range(n):
                el, nums[i] = nums[i], el

        n = len(nums)
        k %= n
        for _ in range(k):
            shift_one()
