from typing import List
import math
from itertools import islice

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = float('-inf')
        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= nums[j]
                max_prod = max(max_prod, prod)
        return max_prod
