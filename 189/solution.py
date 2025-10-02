# 189. Rotate Array
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k == 0:
            return
        start = 0
        i = start
        prev = nums[i]
        for _ in range(n):
            i = (i + k) % n
            tmp = nums[i]
            nums[i] = prev
            prev = tmp
            if i == start:
                i += 1
                prev = nums[i]
                start = i
            
