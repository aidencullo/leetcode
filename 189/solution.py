# 189. Rotate Array
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(lst, l, r):
            while l < r:
                lst[l], lst[r] = lst[r], lst[l]
                l += 1
                r -= 1

        n = len(nums)
        k %= n
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
