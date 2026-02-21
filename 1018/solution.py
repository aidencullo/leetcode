from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        running = 0
        res = []
        for i, bit in enumerate(nums):
            running *= 2
            running += bit
            res.append(running % 5 == 0)

        return res
            
