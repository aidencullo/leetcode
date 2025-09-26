# 189. Rotate Array
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k %= n

        if k == 0:
            return

        if n % k == 0:
            self.rotateModulo(nums, k)
        else:
            self.rotateNonModulo(nums, k)            

    def rotateModulo(self, nums: List[int], k: int) -> None:
        n = len(nums)
        cycle_len = n // k
        for i in range(k):
            pos = i
            el = nums[pos]
            for j in range(cycle_len):
                pos += k
                pos %= n
                next_el = nums[pos]
                nums[pos] = el
                el = next_el

    def rotateNonModulo(self, nums: List[int], k: int) -> None:
        n = len(nums)
        pos = 0
        el = nums[pos]
        for i in range(n):
            pos += k
            pos %= n
            next_el = nums[pos]
            nums[pos] = el
            el = next_el
