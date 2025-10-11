class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        import math
        minimum_sum = math.inf
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                width = j - i + 1
                if width >= l and width <= r and current_sum > 0:
                    minimum_sum = min(minimum_sum, current_sum)
        return minimum_sum if minimum_sum != math.inf else -1
