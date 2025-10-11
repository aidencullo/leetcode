import math
from functools import reduce

def array_gcd(arr):
    return reduce(math.gcd, arr)

def array_lcm(arr):
    def lcm(a, b):
        return a * b // math.gcd(a, b)
    return reduce(lcm, arr)

class Solution:
    def maxLength(self, nums: List[int]) -> int:

        def is_product_equivalent(arr):
            return math.prod(arr) == array_lcm(arr) *  array_gcd(arr)
        
        n = len(nums)
        max_length = -math.inf
        for i in range(n):
            for j in range(i, n):
                if is_product_equivalent(nums[i: j + 1]):
                    max_length = max(max_length, j - i + 1)
        return max_length
