class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        import math
        minimum_sum = math.inf
        for subarray_length in range(l, r + 1):
            for i in range(n):
                if i + subarray_length <= n:
                    current_sum = sum(nums[i: i + subarray_length])
                    if current_sum > 0:
                        minimum_sum = min(minimum_sum, current_sum)
        return minimum_sum if minimum_sum != math.inf else -1
