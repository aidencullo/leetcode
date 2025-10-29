class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        min_sum = math.inf
        n = len(nums)
        for i in range(n):
            middle = nums[i]
            min_left = min(nums[:i]) if i > 0 else math.inf
            min_right = min(nums[i + 1:]) if i < n - 1 else math.inf
            if min_left < middle and min_right < middle:
                min_sum = min(min_sum, min_left + middle + min_right)
        return min_sum if min_sum != math.inf else -1
