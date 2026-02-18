from typing import List


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        def concat_value(x, y):
            return int(str(x) + str(y))
            
        n = len(nums)
        l, r = 0, n - 1
        res = 0

        while l < r:
            res += concat_value(nums[l], nums[r])
            l += 1
            r -= 1

        if l == r:
            res += nums[l]

        return res
