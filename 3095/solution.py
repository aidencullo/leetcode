import math

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        shortest = math.inf
        for start in range(n):
            bitwise_or = 0
            for end in range(start, n):
                bitwise_or |= nums[end]
                if bitwise_or >= k:
                    shortest = min(shortest, end - start + 1)
        return shortest if shortest != math.inf else -1
