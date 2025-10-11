import math
from functools import reduce


class Solution:
    def maxLength(self, nums: List[int]) -> int:

        def is_product_equivalent(arr):
            return math.prod(arr) == array_lcm(arr) * array_gcd(arr)

        n = len(nums)
        max_length = -math.inf
        for i in range(n):
            x = nums[i]
            product = 1
            lcm = x
            gcd = x
            for j in range(i, n):
                y = nums[j]
                product *= y
                lcm = math.lcm(lcm, y)
                gcd = math.gcd(gcd, y)
                if product == gcd * lcm:
                    max_length = max(max_length, j - i + 1)
        return max_length
