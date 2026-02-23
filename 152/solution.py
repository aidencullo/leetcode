from typing import List
import math
from itertools import islice

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = float('-inf')
        for i in range(n):
            for j in range(i + 1, n + 1):
                max_prod = max(max_prod, math.prod(islice(nums, i, j)))
        return max_prod
